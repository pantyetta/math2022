import sympy as sp
import numpy as np
import math


def original():
    print("\
    |d0 d1|    |x|\n\
    |     | ≡ | | (mode N)\n\
    |d2 d3|    |y|\n\
    -----------------------\
    ")

    data = [[0, 0], [0, 0]]
    inverse_data = [[0, 0], [0, 0]]

    for i in range(0, 2):  # ----input
        for j in range(0, 2):
            data[i][j] = int(input(f"d{i + j}: "))

    x = int(input("x: "))  # 追加
    y = int(input("y: "))  # 追加

    N = int(input("mod: "))

    print("\nA行列")  # --- 入力の確認
    for i in range(0, 2):
        print("| ", end='')
        for j in range(0, 2):
            print(f"{data[i][j]} ", end='')
        print("|")

    data_siki = data[0][0] * data[1][1] - data[0][1] * data[1][0]
    print(f"{data_siki % N} ≡ 1(mod {N})\n")

    # ---- ここから ユークリッド互除法

    a = []  # 割られる数
    b = []  # 割る数
    q = []  # 商
    r = []  # あまり

    i = 0  # 値の初期化

    a.append(data_siki % N)  # 初期値の追加
    b.append(N)

    while True:
        q.append(a[i] // b[i])
        r.append(a[i] % b[i])
        a.append(b[i])  # 割った数=>割られる数
        b.append(r[i])  # あまり=>割る数
        print(f"({i}) {a[i]} = {b[i]} * {q[i]} + {r[i]}")
        if r[i] == 0:
            break
        i += 1  # リストの位置を更新

    print("最大公約数: ", b[i])

    # --- ここから 一次不等式

    num1_x = 1
    num2_x = -q[i - 1]
    print(f"({i - 1}) 1 = {a[i - 1]} * {num1_x} + {b[i - 1]} * {num2_x}")

    for i in reversed(range(0, len(a) - 2)):  # リストの最後-2から0まで
        num0_x = num1_x  # 余り以外のかけ数を保存

        # 余り内を計算
        # r(1) = a * a_x + q * -q_x
        # step1) 1 = a[i] * num1_x + num2 * -num2_x(i)
        # step2) 1 = a[i] * num1_x + ( a[i] * num1_x + num2 * -num2_xin-1) ) * num2_x(i))

        num1_x = num2_x
        num2_x *= -q[i]
        num2_x += num0_x  # 余り内の計算に保存したかけ数を追加

        print(f"({i}) 1 = {a[i]} * {num1_x} + {b[i]} * {num2_x}")

    print("x = {} y = {}".format(num1_x, num2_x))

    inverse_data_siki = num1_x % N  # インバース|A|
    print(f"\nインバース|A|≡{inverse_data_siki} (mod {N})")

    # --- 逆行列を求める
    for i in range(0, 2):
        for j in range(0, 2):
            if i == j:
                inverse_data[i][j] = (data[abs(1 - i)][abs(1 - j)] * inverse_data_siki) % N  # 0,1反転 0 or |-1|
            else:
                inverse_data[i][j] = (-data[i][j] * inverse_data_siki) % N

    print("Aの逆行列")
    for i in range(0, 2):
        print("| ", end='')
        for j in range(0, 2):
            print(f"{inverse_data[i][j]} ", end='')
        print("|")

    x_anser = inverse_data[0][0] * x + inverse_data[0][1] * y
    y_anser = inverse_data[1][0] * x + inverse_data[1][1] * y

    print(f"\n(x, y) ≡ ({x_anser}, {y_anser})(mod {N})")
    print("最小正剰余表記 ↓")
    print(f"(x, y) ≡ ({x_anser % N}, {y_anser % N})(mod {N})")


Determinant = lambda data: data[0][0] * data[1][1] - data[0][1] * data[1][0]
Inverse_arr = lambda data: np.array([[data[1][1], -data[0][1]], [-data[1][0], data[0][0]]])


def main():
    data = np.zeros((2, 2))
    r = np.zeros(2)

    print("\
|0,0 0,1||x|    |r1|\n\
|       || | ≡  |  | (mode N)\n\
|1,0 1,1||y|    |r2|\n\
-------------------------------\
    ")

    for i in range(0, 2):  # ----input
        for j in range(0, 2):
            data[i][j] = int(input(f"{i},{j}: "))
    r[0] = int(input("r1: "))  # 追加
    r[1] = int(input("r2: "))  # 追加

    modN = int(input("mod: "))
    data_siki = int(Determinant(data) % modN)

    data_in = (Inverse_arr(data) * sp.gcdex(data_siki, modN)[0]) % modN  # 逆行列 * 一次不定式
    answer = np.dot(data_in, r) % modN

    print("#### result ####")
    print(f"x = {int(answer[0])}, y = {int(answer[1])}")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
