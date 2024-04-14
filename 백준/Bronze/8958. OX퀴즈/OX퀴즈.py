n = int(input())

for i in range(n):
    a = input()
    s = 0
    sc = 0
    for j in a:
        if j == 'O':
            s += 1
        else:
            s = 0
        sc += s
    print(sc)