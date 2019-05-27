from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

file_in = open("encrypted_data.bin", "rb")
ciphertext = file_in.read()

# decrypt with private key
private_key = RSA.import_key(open("private.pem").read())
cipher_rsa = PKCS1_OAEP.new(private_key)
data = cipher_rsa.decrypt(ciphertext)

print(data.decode("utf-8"))