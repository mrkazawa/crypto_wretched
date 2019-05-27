from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Cipher import PKCS1_OAEP

import utils

# ------------------------- RSA Keys ------------------------- //
server_prv = RSA.import_key(open("server_prv.pem").read())
server_pub = RSA.import_key(open("server_pub.pem").read())
# assuming we already know the client pub key
client_pub = RSA.import_key(open("client_pub.pem").read())

# ------------------------- Toy DH Keys ------------------------- //
c_public = 197
s_public = 151
s_private = 157

"""
To make it simple, we dont use communication channel,
but we exchange the key through file creation.
"""

# get the encrypted partial key from the server
f = open("partial_client.bin", "rb")
ciphertext = f.read()
# get the signature form the server
f = open("partial_client.sig", "rb")
signature = f.read()

# verify the originality
h = SHA256.new(ciphertext)
try:
    pkcs1_15.new(client_pub).verify(h, signature)
except (ValueError, TypeError):
    print("The signature is not valid.")

# decrypt the partial key
cipher_rsa = PKCS1_OAEP.new(server_prv)
data = cipher_rsa.decrypt(ciphertext)
partial_key = int(data.decode("utf-8"))

# generate the full key of diffie-hellman, full key is the session key
full_key = utils.generate_full_key(partial_key, s_private, s_public)
server_key = str(full_key).encode("utf-8")
f = open("server.key", "wb")
f.write(server_key)