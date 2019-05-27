from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = "I met aliens in UFO. Here is the map.".encode("utf-8")

# generate symmetric key
key = get_random_bytes(16)
file_out = open("aes.key", "wb")
file_out.write(key)

cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

file_out = open("encrypted.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]