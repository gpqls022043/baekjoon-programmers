n = int(input())
coor = []

for i in range(n):
    x, y = map(int, input().split())
    coor1 = [x, y]
    coor.append(coor1)

coor.sort(key = lambda x : (x[0], x[1]))

for j in range(n):
    print(*coor[j])