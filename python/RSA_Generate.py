from Crypto.PublicKey import RSA
from os import path
from getpass import getpass

userRoot = path.expanduser("~")

Buffer = 2048
savepath = userRoot + "\.ssh\id_rsa"
passphrase = ""

input_value = input("Buffer size (default is 2048):")   # バッファサイズ
if input_value: # 空白時デフォルト使用
    if input_value.isdecimal():     #数値に変換できる場合は変更
        Buffer = int(input_value)   # +整数のみ変換
    else:
        print("Error: Buffer size is bad value")
        quit(0)

input_savepath = input(f"save key path ({savepath}):")  # 保存場所
if input_savepath:  # 空白時デフォルト使用
    if path.isdir(input_savepath.rstrip(input_savepath.split("\\")[-1])):   # user\.ssh\id_rsa のid_rsa部分の切り取り
        savepath = input_savepath                                           # フォルダー確認に保存けってい
    else:
        print(f"Error: not found folder {input_savepath}")
        quit(0)

while True:
    input_pass = getpass("passphrase (empty for no passphrase):")   # パスフレーズ  getpassでコンソールに表示されない

    if not input_pass:  # 空白なら抜ける
        break
    input_pass_sec = getpass("passphrase again:")   # 確認用に２回入力
    if input_pass == input_pass_sec:
        passphrase = input_pass
        break

# 秘密鍵の作成
key = RSA.generate(Buffer)

print("Generate Private Key...")
if passphrase:
    private_key = key.export_key(format="PEM", passphrase=passphrase, protection="DER")
else:
    private_key = key.export_key(format="PEM")
file_out = open(f"{savepath}", "wb")
file_out.write(private_key)
file_out.close()

# 公開鍵の作成
print("Generate Public Key...")
public_key = key.publickey().export_key(format="OpenSSH")
file_out = open(f"{savepath}.pub", "wb")
file_out.write(public_key)
file_out.close()
