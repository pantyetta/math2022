from Crypto.PublicKey import RSA
from os import path
from getpass import getpass


def getBufferSize(default=2048):
    input_value = input("Buffer size (default is 2048):")  # バッファサイズ
    if input_value:  # 空白時デフォルト使用
        if input_value.isdecimal():  # 数値に変換できる場合は変更
            return int(input_value)  # +整数のみ変換
        else:
            print("Error: Buffer size is bad value")
            quit(0)
    return default


def getPath(default=path.expanduser("~") + r"\.ssh\id_rsa"):
    input_savepath = input(f"save key path ({default}):")  # 保存場所
    if input_savepath:  # 空白時デフォルト使用
        if path.isdir(input_savepath.rstrip(input_savepath.split("\\")[-1])):  # user\.ssh\id_rsa のid_rsa部分の切り取り
            return input_savepath  # フォルダー確認に保存けってい
        else:
            print(f"Error: not found folder {input_savepath}")
            quit(0)
    else:
        if path.isdir(default.rstrip(default.split("\\")[-1])):  # user\.ssh\id_rsa のid_rsa部分の切り取り
            return default  # フォルダー確認に保存けってい
        else:
            print(f"Error: not found folder {input_savepath}")
            quit(0)


def getPassphrase():
    passphrase = ""
    while True:
        input_pass = getpass("passphrase (empty for no passphrase):")  # パスフレーズ  getpassでコンソールに表示されない
        if not input_pass:  # 空白なら抜ける
            break

        input_pass_sec = getpass("passphrase again:")  # 確認用に２回入力
        if input_pass == input_pass_sec:
            passphrase = input_pass
            break
    return passphrase


def saveFile(rsa_key, file_path, mode=0):
    if mode == 0:
        fw = open(f"{file_path}", "wb")
    elif mode == 1:
        fw = open(f"{file_path}.pub", "wb")
    else:
        raise Exception("mode is out of range")
    fw.write(rsa_key)
    fw.close()


def main():

    print("Generate Private Key...")
    # 秘密鍵の作成
    key = RSA.generate(getBufferSize())
    savepath = getPath()
    passphrase = getPassphrase()

    if passphrase:
        private_key = key.export_key(format="PEM", passphrase=passphrase, protection="DER")
    else:
        private_key = key.export_key(format="PEM")
    saveFile(private_key, savepath, 0)

    # 公開鍵の作成
    print("Generate Public Key...")
    public_key = key.publickey().export_key(format="OpenSSH", protection="DER")
    saveFile(public_key, savepath, 1)


if __name__ == '__main__':
    main()
