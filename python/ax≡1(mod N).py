import sympy as sp


def original():
    print("ax ≡ 1 (mod N)")
    input_a = int(input("a: "))
    N = int(input("mod: "))

    print("--- --- --- ---")
    print(f"{input_a}x ≡ 1 (mod {N})")
    print(f"{input_a}x + {N}y = 1")

    # ---- ここから下は 一次不等式のやつ

    a = []  # 割られる数
    b = []  # 割る数
    q = []  # 商
    r = []  # あまり

    i = 0  # 値の初期化

    a.append(input_a)
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

    num1_x = 1
    num2_x = -q[i - 1]  # リストの最後-2の値をセット
    print(f"({i - 1}) 1 = {a[i - 1]} * {num1_x} + {b[i - 1]} * {num2_x}")

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

        print(f"({i}) 1 = {a[i]} * {num1_x} + {b[i]} * {num2_x}")

    print("\nx = {} y = {}".format(num1_x, num2_x))

    print(f"x≡{num1_x % N} (mod {N})")


def main():
    print("ax ≡ 1 (mod N)")
    input_a = int(input("a (1537): "))
    modN = int(input("mod N (1457): "))

    print("--- input result ---")
    print(f"{input_a}x ≡ 1 (mod {modN})")
    print(f"{input_a}x + {modN}y = 1")

    answer = sp.gcdex(input_a, modN)
    print("--- result ---")
    print(f"x≡{answer[0]%modN} (mod {modN})")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
