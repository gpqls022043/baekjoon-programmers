n = int(input())
b = []
plus = 0

for i in range(n):
    minus = n - i
    minus1 = list(map(int, str(minus)))
    for j in range(len(minus1)):
        plus = plus + minus1[j]
    if minus + plus == n:
        b.append(minus)
        plus = 0
    else:
        plus = 0
        continue
if len(b) == 0:
    print('0')
else:    
    print(min(b))