import sys
N,K = map(int, sys.stdin.readline().split())
start = list(map(int,list(sys.stdin.readline().strip())))
stack = []

for i in range(N):
    while K > 0 and stack and stack[-1] < start[i]:
        stack.pop()
        K -= 1
    stack.append(start[i])

for i in range(K):
    stack.pop()

print(''.join(map(str,stack)))

# for i in range(K):
#     for j in range(N-1-i):
#         if start[j] < start[j+1]:
#             del start[j]
#             break
#     if len(start) == N-i:
#         del start[N-1-i]

# print(*start)