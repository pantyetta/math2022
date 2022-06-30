from Crypto.PublicKey import RSA

Buffer = 2048

input_value = input("Buffer (default is 2048):")
if input_value != "":
    Buffer = int(input_value)

# 秘密鍵の作成
key = RSA.generate(Buffer)
private_key = key.export_key(format="PEM", passphrase="passphrase", protection="DER")
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()

# 公開鍵の作成
public_key = key.publickey().export_key(format="OpenSSH")
file_out = open("public.pem", "wb")
file_out.write(public_key)
file_out.close()