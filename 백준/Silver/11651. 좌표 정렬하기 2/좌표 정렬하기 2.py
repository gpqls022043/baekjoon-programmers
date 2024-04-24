array = []

for i in range(int(input())):
    x, y = map(int, input().split())
    array.append([x, y])
    
array.sort(key=lambda b : (b[1], b[0]))

for j in range(len(array)):
    print(*array[j])