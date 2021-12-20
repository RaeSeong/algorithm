import sys
N = int(sys.stdin.readline())
command = []
queue = []

def do_command(command, queue):
    do = command[0]
    if do == 'push':
        push(command, queue)
    elif do == 'pop':
        pop(queue)
    elif do == 'size':
        size(queue)
    elif do == 'empty':
        empty(queue)
    elif do == 'front':
        front(queue)
    elif do == 'back':
        back(queue)

def back(queue):
    if not queue:
        print(-1)
    else:
        print(queue[len(queue)-1])

def front(queue):
    if not queue:
        print(-1)
    else:
        print(queue[0])

def size(queue):
    print(len(queue))

def empty(queue):
    if not queue:
        print(1)
    else:
        print(0)

def pop(queue):
    if not queue:
        output = -1
    else:
        output = queue.pop(0)
    print(output)

def push(command, queue):
    queue.append(command[1])

for i in range(N):
    command.append(sys.stdin.readline().split())
    do_command(command[i], queue)
# for j in range(N):
#     do_command(command[j], queue)