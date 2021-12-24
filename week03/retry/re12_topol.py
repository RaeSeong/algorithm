import sys
from collections import deque
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
build = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
connect = [[] for _ in range(N+1)]
indgr = [0]*(N+1)
need = [[0]*(N+1) for _ in range(N+1)]
for i in build:
    connect[i[1]].append([i[0],i[2]])
    indgr[i[0]] += 1

queue = []
basic = []
for i in range(1,N+1):
    if indgr[i] == 0:
        queue.append(i)
        basic.append(i)

while queue:
    a = queue.pop()
    for next, cnt in connect[a]:
        if a in basic:
            need[next][a] += cnt
        else:
            for i in range(1,N+1):
                need[next][i] += need[a][i]*cnt
        indgr[next] -= 1
        if indgr[next] == 0:
            queue.append(next)

for i in range(1,N+1):
    if need[N][i] != 0:
        print(i, need[N][i])







###################################
# need = [[] for _ in range(N+1)]

# for i in build:
#     node[i[1]].append([i[0],i[2]])
#     inde[i[0]] += 1

# print(inde)
# queue = deque([])
# for i in range(1,N+1):
#     if inde[i] == 0:
#         queue.append(i)
#     else:
#         need[i] = [0]*(N+1)

# while queue:
#     i = queue.popleft()
#     for a in node[i]:
#         part, ea = a
#         print(need[part], part, i)
#         if need[i]:
#             for j in need[part]:
#                 need[part][i] = need[i][j]*ea
#         else:
#             need[part][i] += ea
#         inde[part] -= 1
#     if inde[part] == 0:
#         queue.append(part)

# print(need)