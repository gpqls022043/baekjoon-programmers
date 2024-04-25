n, k = map(int, input().split())
a = []
k1 = k - 1
k -= 1

yo = [i for i in range(1, n + 1)]

while (len(yo) != 0):
    if k1 < len(yo):
        a.append(yo[k1])
        del yo[k1]
        k1 += k
    else:
        k1 = k1 - len(yo)
        if k1 < len(yo):
            a.append(yo[k1])
            del yo[k1]
            k1 += k
        else:
            while (len(yo) != 0):
                try:
                    k1 = k1 - len(yo)
                    a.append(yo[k1])
                    del yo[k1]
                    k1 += k
                except:
                    continue
                    
print('<', end="")
print(", ".join(map(str, a)), end="")
print('>')