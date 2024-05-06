n, m = map(int, input().split())
a = []
b = []
p = []
for i in range(n):
    a.append(input().split())
for i in range(n):
    b.append(input().split())
for i in range(n):
    p.append([])
    
for i in range(n):
    for j in range(m):
        p[i].append(int(a[i][j]) + int(b[i][j]))

for i in range(n):
    print(*p[i])