from Crypto.PublicKey import RSA

key = RSA.generate(2048)
private_key = key.export_key()
file_out = open("privatekey.pem", "wb")
file_out.write(private_key); file_out.close()
print(private_key)

public_key = key.publickey().export_key()
file_out = open("publickey.pem", "wb")
file_out.write(public_key); file_out.close()
print(public_key)