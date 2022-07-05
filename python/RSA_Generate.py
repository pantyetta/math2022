from Crypto.PublicKey import RSA
from os.path import expanduser
from getpass import getpass

UserRoot = expanduser("~")
Buffer = 2048
passphrase = ""

input_value = input("Buffer (default is 2048):")
if input_value:
    Buffer = int(input_value)

while True:
    input_pass = getpass("passphrase (empty for no passphrase):")
    if not input_pass:  # 空白なら抜ける
        break
    input_pass_sec = getpass("passphrase again:")
    if input_pass == input_pass_sec:
        passphrase = input_pass
        break

# 秘密鍵の作成
key = RSA.generate(Buffer)

print("Generate Private Key...")
private_key = key.export_key(format="PEM", passphrase=passphrase, pkcs=1 , protection="DER")
file_out = open(f"{UserRoot}\id_rsa", "wb")
file_out.write(private_key)
file_out.close()

# 公開鍵の作成
print("Generate Public Key...")
public_key = key.publickey().export_key(format="OpenSSH")
file_out = open(f"{UserRoot}\id_rsa.pub", "wb")
file_out.write(public_key)
file_out.close()
