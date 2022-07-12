import conversion
import numpy as np


def encrypt():
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

    raw_value_arr = conversion.text_decode(text, text_template)  # テキストを数値に変換
    value_arr = conversion.value_encode(raw_value_arr)  # ２次元配列形式に変更
    row_answer = np.dot(Key, value_arr) % modN    # 行列の掛け算
    answer = conversion.value_decode(row_answer)    # 単一配列に変換
    print("#### result ####")
    for t in conversion.text_encode(answer, text_template):
        print(t, end='')


if __name__ == '__main__':
    try:
        encrypt()
    except KeyboardInterrupt:
        pass
