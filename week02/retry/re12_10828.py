import sys
N = int(sys.stdin.readline())
command = [list(sys.stdin.readline().split()) for _ in range(N)]
stack = []

for i in range(N):
    do = command[i][0]
    if do == 'push':
        stack.append(command[i][1])
    elif do == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif do == 'size':
        print(len(stack))
    elif do == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif do == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            top = stack.pop()
            print(top)
            stack.append(top)

