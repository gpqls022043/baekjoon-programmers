code = list(map(int, input().split()))
a = []
d = []

for i in range(1, 9):
    a.append(i)
for j in range(8):
    d.append(8 - j)
if code == a:
    print('ascending')
elif code == d:
    print('descending')
else:
    print('mixed')