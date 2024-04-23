k = int(input())
a = []
plus = 0

for i in range(k):
    num = int(input())
    if num != 0:
        a.append(num)
    else:
        del a[len(a) - 1]
for j in range(len(a)):
    plus = plus + a[j]
print(plus)