n = int(input())
count = 1
cycle = 0

for i in range(n):
    count = count + 6*i
    if count >= n:
        cycle = i + 1
        count = count - 6*i
        break
    else:
        continue
print(cycle)