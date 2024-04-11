n = int(input())

for i in range(n):
    star = '*' * (n - i)
    space = ' ' * i
    print(space+star)