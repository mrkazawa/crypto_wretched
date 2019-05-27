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

# generate the partial key of diffie-hellman
partial_key = utils.generate_partial_key(c_private, c_public, s_public)
data = str(partial_key).encode("utf-8")

# encrypt the partial key
cipher_rsa = PKCS1_OAEP.new(server_pub)
chipertext = cipher_rsa.encrypt(data)
f = open("partial_client.bin", "wb")
f.write(chipertext)

# hash the ciphertext and sign
h = SHA256.new(chipertext)
signature = pkcs1_15.new(client_prv).sign(h)
f = open("partial_client.sig", "wb")
f.write(signature)