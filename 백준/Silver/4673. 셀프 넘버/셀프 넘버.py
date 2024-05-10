def d(n):
    n1 = list(str(n))
    answer = n
    for i in range(len(n1)):
        answer += int(n1[i])
    return answer

self_num = [x for x in range(1, 10001)]

for i in range(1, 10001):
    dn = d(i)
    if dn <= 10000:
        try:
            self_num.pop(self_num.index(dn))
        except:
            continue
    else:
        continue

print(*self_num, sep='\n')