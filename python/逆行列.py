
print("\
|d0 d1|\n\
|d2 d3|\n\
--------\
")

data = [[0,0],[0,0]]

for i in range(0, 2): # ----input
  for j in range(0, 2):
    data[i][j] = int(input(f"d{i + j}: "))

N = int(input("mod: "))

print("A行列")
for i in range(0, 2):
  print("| ", end='')
  for j in range(0, 2):
    print(f"{data[i][j]} ", end='')
  print("|")

data_retu = data[0][0] * data[1][1] - data[0][1] * data[1][0]
print(f"{data_retu%N} ≡ 1(mod {N})")


# ---- ここから下は 一次不等式のやつ

a = []  #割られる数
b = []  #割る数
q = []  #商
r = []  #あまり

i = 0 #値の初期化

a.append(data_retu%N)
b.append(N)

while True:
  q.append(a[i] // b[i]) 
  r.append(a[i] % b[i]) 
  a.append(b[i]) # 割った数=>割られる数
  b.append(r[i]) # あまり=>割る数
  print(f"({i}) {a[i]} = {b[i]} * {q[i]} + {r[i]}")
  if r[i] == 0:
    break
  i += 1         # リストの位置を更新

print("最大公約数: ", b[i])

num1_x = 1
num2_x = -q[i-1]  # リストの最後-2の値をセット
print(f"({i-1}) 1 = {a[i-1]} * {num1_x} + {b[i-1]} * {num2_x}")

for i in reversed(range(0, len(a)-3)):  # リストの最後-3から0まで
    
    # r(1) = a[i] * 1 + b[i] * -q[i]
    # step1) 1 = 5 * 1 + 2 * -2
    # step2) 1 = 5 * 1 + ( 12 * 1 + 5 * -2 ) * -2
    #      ) 1 = 12 * -2 + 5 * 5
    # step3) 1 = 12 * -2 + ( 17 * 1 + 12 * -1 ) * 5
    #      ) 1 = 17 * 5 + 12 * -7
    
    num0_x = num1_x # aにかかっている前の係数を保存
    num1_x = num2_x # aにかかる係数はひとつ前のbの係数
    num2_x *= -q[i] # ひとつ前のbの係数に新しい係数をかける
    num2_x += num0_x# 前のaにかかっていた係数をプラス

    print(f"({i}) 1 = {a[i]} * {num1_x} + {b[i]} * {num2_x}")


print("\nx = {} y = {}".format(num1_x, num2_x))

print(f"x≡{num1_x%N} (mod {N})")

inverse_data_siki = num1_x % N


print("--- --- --- ----")
print(f"|A|^1≡{inverse_data_siki} (mod {N})")

inverse_data = [[0,0],[0,0]]

for i in range(0, 2):
  for j in range(0, 2):
    if i == j:
      inverse_data[i][j] = (data[abs(1-i)][abs(1-j)] * inverse_data_siki) % N
    else:
      inverse_data[i][j] = (-data[i][j] * inverse_data_siki) % N

print("Aの逆行列")
for i in range(0, 2):
  print("| ", end='')
  for j in range(0, 2):
    print(f"{inverse_data[i][j]} ", end='')
  print("|")
