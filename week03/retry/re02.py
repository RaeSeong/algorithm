import sys
computer = int(sys.stdin.readline())
network = int(sys.stdin.readline())
edges = [list(map(int,sys.stdin.readline().split())) for _ in range(network)]
LAN = [[] for _ in range(computer+1)]

for i in edges:
    LAN[i[0]].append(i[1])
    LAN[i[1]].append(i[0])

# def dfs(v):
#     cnt = 0
#     for i in LAN[v]:
#         if i not in virus:
#             virus.append(i)
#             cnt += dfs(i)
#             cnt += 1
#     return cnt
        
# virus = [1]
# result = 0
# result += dfs(1)

# print(result)

from collections import deque
queue = deque()
chk = []
def bfs(v):
    queue.append(v)
    while queue:
        a = queue.popleft()
        if a not in chk:
            chk.append(a)
            for i in LAN[a]:
                queue.append(i)

bfs(1)
print(len(chk)-1)