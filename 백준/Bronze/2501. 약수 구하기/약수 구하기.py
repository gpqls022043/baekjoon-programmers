k, n = map(int, input().split())
measure = []

for i in range(1, k + 1):
    if k % i == 0:
        measure.append(i)
    else:
        continue
if len(measure) >= n:
    print(measure[n - 1])
else:
    print(0)