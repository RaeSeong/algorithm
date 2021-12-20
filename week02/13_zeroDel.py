import sys
K = int(sys.stdin.readline())
stack = []
for i in range(K):
    N = int(sys.stdin.readline())
    if N == 0:
        del stack[len(stack)-1]
    else:
        stack.append(N)

print(sum(stack))