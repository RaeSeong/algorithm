import sys
N,M,V = map(int,sys.stdin.readline().split())
graph = {}
chk_dfs = []
chk_bfs = []
for i in range(M):
    x,y = map(int,sys.stdin.readline().split())
    if x not in graph:
        graph[x] = [y]
    else:
        graph[x].append(y)

    if y not in graph:
        graph[y] = [x]
    else:
        graph[y].append(x)

def dfs(v,chk_dfs=[]):
    if v not in chk_dfs:
        chk_dfs.append(v)
        graph[v].sort()
        for w in graph[v]:
            dfs(w,chk_dfs)
    return chk_dfs

def bfs(start):
    chk_bfs = [start]
    queue = [start]
    while queue:
        v = queue.pop(0)
        # chk_bfs.append(v)
        for w in graph[v]:
            if w not in chk_bfs:
                chk_bfs.append(w)
                queue.append(w)
    return chk_bfs


print(" ".join(map(str,dfs(V))))
print(" ".join(map(str,bfs(V))))
