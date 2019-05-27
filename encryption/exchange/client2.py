from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Cipher import PKCS1_OAEP

import utils

# ------------------------- RSA Keys ------------------------- //
client_prv = RSA.import_key(open("client_prv.pem").read())
client_pub = RSA.import_key(open("client_pub.pem").read())
# assuming we already know the server pub key
server_pub = RSA.import_key(open("server_pub.pem").read())

# ------------------------- Toy DH Keys ------------------------- //
c_public = 197
c_private = 199
s_public = 151

"""
To make it simple, we dont use communication channel,
but we exchange the key through file creation.
"""

# get the encrypted partial key from the server
f = open("partial_server.bin", "rb")
ciphertext = f.read()
# get the signature form the server
f = open("partial_server.sig", "rb")
signature = f.read()

# verify the originality
h = SHA256.new(ciphertext)
try:
    pkcs1_15.new(server_pub).verify(h, signature)
except (ValueError, TypeError):
    print("The signature is not valid.")

# decrypt the partial key
cipher_rsa = PKCS1_OAEP.new(client_prv)
data = cipher_rsa.decrypt(ciphertext)
partial_key = int(data.decode("utf-8"))

# generate the full key of diffie-hellman, full key is the session key
full_key = utils.generate_full_key(partial_key, c_private, s_public)
client_key = str(full_key).encode("utf-8")
f = open("client.key", "wb")
f.write(client_key)