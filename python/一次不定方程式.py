import sympy as sy


def old(x, y):
    a = []  # 割られる数
    b = []  # 割る数
    q = []  # 商
    r = []  # あまり

    i = 0  # 値の初期化

    a.append(x)
    b.append(y)

    while True:
        q.append(a[i] // b[i])
        r.append(a[i] % b[i])
        a.append(b[i])  # 割った数=>割られる数
        b.append(r[i])  # あまり=>割る数
        # print(f"({i}) {a[i]} = {b[i]} * {q[i]} + {r[i]}")
        if r[i] == 0:
            break
        i += 1  # リストの位置を更新

    # print("最大公約数: ", b[i])

    num1_x = 1
    num2_x = -q[i - 1]  # リストの最後-2の値をセット
    # print(f"({i - 1}) 1 = {a[i - 1]} * {num1_x} + {b[i - 1]} * {num2_x}")

    for i in reversed(range(0, len(a) - 3)):  # リストの最後-3から0まで

        # r(1) = a[i] * 1 + b[i] * -q[i]
        # step1) 1 = 5 * 1 + 2 * -2
        # step2) 1 = 5 * 1 + ( 12 * 1 + 5 * -2 ) * -2
        #      ) 1 = 12 * -2 + 5 * 5
        # step3) 1 = 12 * -2 + ( 17 * 1 + 12 * -1 ) * 5
        #      ) 1 = 17 * 5 + 12 * -7

        num0_x = num1_x  # aにかかっている前の係数を保存
        num1_x = num2_x  # aにかかる係数はひとつ前のbの係数
        num2_x *= -q[i]  # ひとつ前のbの係数に新しい係数をかける
        num2_x += num0_x  # 前のaにかかっていた係数をプラス

        # print(f"({i}) 1 = {a[i]} * {num1_x} + {b[i]} * {num2_x}")

    print(" x= {}, y= {}".format(num1_x, num2_x))

    print("--- 一般解 ---")
    print(" x= {} + {}t".format(num1_x, y))
    print(" y= {} - {}t".format(num2_x, x))


def main(x, y):
    answer = sy.gcdex(x, y)
    print(f" x= {answer[0]}, y= {answer[1]}")
    print("--- 一般解 ---")
    print(f" x= {answer[0]} + {y}t")
    print(f" y= {answer[1]} - {x}t")


if __name__ == '__main__':
    x = (int(input("X: ")))
    y = (int(input("y: ")))

    print("### used library ###")
    main(x, y)
    print("### end library ###\n")

    print("### original ###")
    old(x, y)
    print("### end original ###")
