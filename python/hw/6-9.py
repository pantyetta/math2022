import conversion
import numpy as np
import sympy as sp
import sys

Determinant = lambda data: int(data[0][0] * data[1][1] - data[0][1] * data[1][0])
Inverse_arr = lambda data: np.array([[data[1][1], -data[0][1]], [-data[1][0], data[0][0]]])
Inverse = lambda Key, modN: ((sp.gcdex(Determinant(Key), modN)[0] % modN) * Inverse_arr(Key)) % modN


def console_input():
    Key = np.zeros((2, 2))
    for i in range(0, 2):  # ----input
        for j in range(0, 2):
            Key[i][j] = int(input(f"Key{i},{j}: "))

    text = input("text: ")
    text_template = input("template: ")
    modN = len(text_template)

    if modN % 2 != 0:
        modN += 1
        text_template += "〓"

    return Key, text, text_template, modN


def console_out(data):
    for i in range(0, 2):
        print("| ", end='')
        for j in range(0, 2):
            print(f"{int(data[i][j])} ", end='')
        print("|")


def search():

    template = input("template: ")
    raw_plain = conversion.text_decode(input("p: "), template)
    raw_crypt = conversion.text_decode(input("c: "), template)

    plain_arr = conversion.value_encode(raw_plain)
    crypt_arr = conversion.value_encode(raw_crypt)

    mod = len(template)

    plain_inv = Inverse(plain_arr, mod)
    Key = np.dot(crypt_arr, plain_inv) % mod
    print("#### result ####")
    print("encryption Key")
    console_out(Key)

    Key_determinant = sp.gcdex(Determinant(Key), mod)[0] % mod
    Key_inv = np.dot(Key_determinant, Inverse_arr(Key)) % mod
    print("decryption key")
    console_out(Key_inv)


def decrypt_key():
    Key, text, text_template, modN = console_input()

    Key = Inverse(Key, modN)

    raw_value_arr = conversion.text_decode(text, text_template)  # テキストを数値に変換
    value_arr = conversion.value_encode(raw_value_arr)  # ２次元配列形式に変更
    row_answer = np.dot(Key, value_arr) % modN    # 行列の掛け算
    answer = conversion.value_decode(row_answer)    # 単一配列に変換
    print("#### result ####")
    for t in conversion.text_encode(answer, text_template):
        print(t, end='')


def convert():
    Key, text, text_template, modN = console_input()

    raw_value_arr = conversion.text_decode(text, text_template)  # テキストを数値に変換
    value_arr = conversion.value_encode(raw_value_arr)  # ２次元配列形式に変更
    row_answer = np.dot(Key, value_arr) % modN    # 行列の掛け算
    answer = conversion.value_decode(row_answer)    # 単一配列に変換
    print("#### result ####")
    print(conversion.text_encode(answer, text_template))


if __name__ == '__main__':
    try:
        args = sys.argv
        if len(args) > 1 and args[1] == "--search":
            print("search mode...")
            search()
        elif len(args) > 1 and args[1] == "--decrypt-key":
            print("generate decrypt mode...")
            decrypt_key()
        else:
            print("convert mode...")
            convert()
    except KeyboardInterrupt:
        pass
