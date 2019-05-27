from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

data = "I met aliens in UFO. Here is the map.".encode("utf-8")

# encyrpt with receiver pub key
recipient_key = RSA.import_key(open("receiver.pem").read())
cipher_rsa = PKCS1_OAEP.new(recipient_key)
chipertext = cipher_rsa.encrypt(data)

# save the encryption result to bin file
file_out = open("encrypted_data.bin", "wb")
file_out.write(chipertext)