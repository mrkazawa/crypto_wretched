from Crypto.PublicKey import RSA

client_key = RSA.generate(2048)
# client private key
f = open("client_prv.pem", "wb")
f.write(client_key.export_key())
# client public key
f = open("client_pub.pem", "wb")
f.write(client_key.publickey().export_key())

server_key = RSA.generate(2048)
# server private key
f = open("server_prv.pem", "wb")
f.write(server_key.export_key())
# server public key
f = open("server_pub.pem", "wb")
f.write(server_key.publickey().export_key())