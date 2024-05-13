import sys

n = int(input())
answer = []

for i in range(n):
    com = sys.stdin.readline().strip()
    if com == 'pop':
        if len(answer) != 0:
            print(answer.pop(len(answer) - 1))
        else:
            print(-1)
    elif com == 'size':
        print(len(answer))
    elif com == 'empty':
        if len(answer) == 0:
            print(1)
        else:
            print(0)
    elif com == 'top':
        if len(answer) != 0:
            print(answer[len(answer) - 1])
        else:
            print(-1)
    else:
        command, num = com.split()
        if command == 'push':
            answer.append(num)