n, m = map(int, input().split())
a = []

for i in range(n):
    a.append(0)  
    
for j in range(m):
    st, nd, rd = map(int, input().split())
    for k in range(st - 1, nd):
        del a[k]
        a.insert(k, rd)
print(*a)