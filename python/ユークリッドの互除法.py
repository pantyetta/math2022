a = (int(input("a: ")))
b = (int(input("b: ")))

i = 0

while True:
  q = a // b
  r = a % b
  print(f"({i}) {a} = {b} * {q} + {r}")
  if r == 0:
    break
  a = b # 割った数=>割られる数
  b = r # あまり=>割る数
  i += 1         # リストの位置を更新

print("最大公約数: ", b)
