t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    floor0 = [x for x in range(1, n + 1)]
    for j in range(k):
        for kk in range(1, n):
            floor0[kk] += floor0[kk - 1]
    print(floor0[-1])