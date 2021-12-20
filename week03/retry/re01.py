import sys
from collections import deque
N,M,V = map(int,sys.stdin.readline().split())
edges = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
node = [[] for _ in range(N+1)]
for i in edges:
    node[i[0]].append(i[1])
    node[i[1]].append(i[0])

for i in node:
    i.sort()

chk_bfs = []
queue = deque([])
def bfs(a):
    queue.append(a)
    while queue:
        b = queue.popleft()
        if b not in chk_bfs:
            chk_bfs.append(b)
            for i in node[b]:
                queue.append(i)

chk_dfs = []
def dfs(a):
    if a not in chk_dfs:
        chk_dfs.append(a)
        for i in node[a]:
            dfs(i)

# chk_dfs2 = []
# def dfs2(a):
#     chk_dfs2.append(a)
#     for i in node[a]:
#         if i not in chk_dfs2:
#             dfs2(i)

# chk_dfs3 = []
# stack = []
# def dfs3(a):
#     stack.append(a)
#     while stack:
#         b = stack.pop()
#         if b not in chk_dfs3:
#             chk_dfs3.append(b)
#             for i in node[b]:
#                 stack.append(i)
bfs(V)
dfs(V)
# dfs2(V)
# for i in node:
#     i.sort(reverse=True)
# dfs3(V)

print(*chk_dfs)
print(*chk_bfs)