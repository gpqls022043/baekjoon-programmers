n = int(input())
a = list(map(int, input().split()))
b = []
count = 0

for i in range(n):
    t = a[i]
    if t == 1:
        continue
    for j in range(1, t + 1):
        if t % j == 0:
            b.append(0)
        else:
            continue
    if len(b) == 2:
        count += 1
        b.clear()
    else:
        b.clear()
print(count)