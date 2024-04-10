n, m = map(int, input().split())
a = []

for i in range(1, n + 1):
    a.append(i)

for j in range(m):
    st, nd = map(int, input().split())
    a[st-1], a[nd - 1] = a[nd - 1], a[st - 1]
print(*a)