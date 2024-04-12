t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    for j in range(99):
        cal = n - (h * j)
        if cal == 0:
            height = h
            num = j
            break
        elif cal < 0:
            height = cal + h
            num = j
            break
    if num < 10:
        print('%d0%d' % (height, num))
    else:
        print('%d%d'% (height, num))