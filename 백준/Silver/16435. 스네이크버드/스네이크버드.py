n, l = map(int, input().split())
fruit = list(map(int, input().split()))
fruit.sort()

for j in range(len(fruit)):
    if l >= fruit[0]:
        l += 1
        del fruit[0]
    else:
        break
print(l)