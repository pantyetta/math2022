import numpy as np
import sympy as sp
import sys
import conversion


def calcKey():

    e = int(input("e: "))
    l = int(input("L: "))

    Euclid_ans = sp.gcdex(e, l)  # 一時不定方程式の計算結果 (x, y, 答え)
    print(Euclid_ans[0] % l)


def crypt():
    N = int(input("n: "))
    E = int(input("e: "))
    text = input("Text: ")
    template = input("文字テンプレート:")

    Nshin = len(template)

    P = conversion.nshin_decode(text, template)
    C = (P ** E) % N
    print(conversion.nshin_encode(np.base_repr(C, Nshin), template))


def decrypt():
    N = int(input("n: "))
    D = int(input("d: "))
    text = input("Text: ")
    template = input("文字テンプレート:")

    Nshin = len(template)

    C = conversion.nshin_decode(text, template)
    P = (C ** D) % N
    print(conversion.nshin_encode(np.base_repr(P, Nshin), template))


if __name__ == '__main__':
    try:
        args = sys.argv
        if len(args) > 1 and args[1] == "--calc-key":
            calcKey()
        elif len(args) > 1 and args[1] == "--decrypt":
            decrypt()
        else:
            crypt()
    except KeyboardInterrupt:
        pass
