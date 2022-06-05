# ["A","E","I","K","M","N","O","R","U","W"]

shiin = ["K", "M", "N", "R", "W"]
boin = ["A", "I", "U", "E", "O"]

f = open("C:/Users/pantyetta/Documents/github/math2022/python/result.txt", "a")

for s1 in range(0, len(shiin)):
    for s2 in range(0, len(shiin)):
        if s1 == s2:
            continue
        for s3 in range(0, len(shiin)):
            if s1 == s3 or s2 == s3:
                continue
            for s4 in range(0, len(shiin)):
                if s1 == s4 or s2 == s4 or s3 == s4:
                    continue
                for b1 in range(0, len(boin)):
                    if (0 < b1 < 4) and (s1 == 4 or s2 == 4 or s4 == 4):  # A,Oの時子音がWだったら次
                        continue
                    for b2 in range(0, len(shiin)):
                        if b1 == b2 or ((0 < b2 < 4) and s3 == 4):  # A,Oの時子音がWだったら次:
                            continue

                        f.write(
                            f"{shiin[s1]}{boin[b1]}{shiin[s2]}{boin[b1]}{shiin[s3]}{boin[b2]}{shiin[s4]}{boin[b1]}\n")

f.close()
