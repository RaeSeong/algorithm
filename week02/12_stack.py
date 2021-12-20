import sys
N = int(sys.stdin.readline())
stack = []

for i in range(N):
    a = sys.stdin.readline().split()
    

    if a[0] == 'push':
        print('------------------------')
        stack.append(a[1])
    if a[0] == 'pop':
        print('pop')
