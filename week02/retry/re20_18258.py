import sys
from collections import deque
N = int(sys.stdin.readline())
command = [sys.stdin.readline().split() for _ in range(N)]
queue = deque([])

for i in command:
    if i[0] == 'push':
        queue.append(i[1])
    elif i[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif i[0] == 'size':
        print(len(queue))
    elif i[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif i[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif i[0] == 'back':
        if not queue:
            print(-1)
        else:
            tmp = queue.pop()
            print(tmp)
            queue.append(tmp)

