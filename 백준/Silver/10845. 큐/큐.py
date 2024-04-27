import sys
import queue

n = int(input())
que = queue.Queue()

for i in range(n):
    com = sys.stdin.readline().strip()
    if com == 'pop':
        if que.empty() == False:
            print(que.get())
        else:
            print(-1)
    elif com == 'size':
        print(que.qsize())
    elif com == 'empty':
        if que.empty() == True:
            print(1)
        else:
            print(0)
    elif com == 'front':
        if que.empty() == False:
            print(que.queue[0])
        else:
            print(-1)
    elif com == 'back':
        if que.empty() == False:
            print(que.queue[-1])
        else:
            print(-1)
    else:
        command, num = com.split()
        if command == 'push':
            que.put(num)