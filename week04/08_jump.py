import sys
from collections import deque as dq
N,M = map(int,sys.stdin.readline().split())
small = [int(sys.stdin.readline().rstrip()) for _ in range(M)]
step = [N+1]*(N+1)
for i in small:
    step[i] = -1


print(step)
if step[N] == N+1:
    print(-1)
else:
    print(step[N])


# move = dq([[1,1]])
# cnt = 1
# repeat = 1
# while move:
#     a,b = move.popleft()
#     repeat -= 1
#     if b <= 0:
#         continue
#     loc = a + b
#     if loc > N or step[loc] == -1:
#         continue
#     step[loc] = min(cnt,step[loc])
#     for i in range(3):
#         move.append([loc,b+i-1])
#     if repeat > 0:
#         continue
#     repeat = len(move)
#     cnt += 1

##############
# for i in range(2,N+1):
#     if step[i] == N+1:
#         continue
#     jump = 1
#     while jump < i - jump**2 + 1:
#         if jump == 1:
#             step[i] = min(step[i-1],step[i-2]) + 1
#         else:
#             step[i] = min(step[i-jump-1],step[i-jump],step[i-jump+1]) + 1
#         jump += 1
#         print(i,jump)