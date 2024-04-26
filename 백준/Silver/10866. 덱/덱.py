from collections import deque
import sys

n = int(input())
dec = deque()

for i in range(n):
    com = sys.stdin.readline().strip()
    if com == 'size' or com == 'empty' or com == 'front' or com == 'back' or com == 'pop_front' or com == 'pop_back':
        if com == 'size':
            print(len(dec))
        elif com == 'empty':
            if len(dec) == 0:
                print(1)
            else:
                print(0)
        elif com == 'front':
            if len(dec) == 0:
                print(-1)
            else:
                print(dec[0])
        elif com == 'back':
            if len(dec) == 0:
                print(-1)
            else:
                print(dec[len(dec) - 1])
        elif com == 'pop_front':
            if len(dec) == 0:
                print(-1)
            else:
                print(dec.popleft())
        elif com == 'pop_back':
            if len(dec) == 0:
                print(-1)
            else:
                print(dec.pop())
    else:
        command, num = com.split()
        if command == 'push_front':
            dec.appendleft(num)
        elif command == 'push_back':
            dec.append(num)