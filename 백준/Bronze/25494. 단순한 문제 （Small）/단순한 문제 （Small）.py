t = int(input())
count = 0 

for t in range(t):
    a, b, c = map(int, input().split())
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            for z in range(1, c + 1):
                if x % y == y % z == z % x:
                    count += 1
                else:
                    continue
    print(count)
    count = 0