import sys
N = int(sys.stdin.readline())
e = int(sys.stdin.readline())
edges = [[0]*(N+1) for _ in range(N+1)]
for _ in range(e):
    x,y = map(int,sys.stdin.readline().split())
    edges[x][y] = 1
    edges[y][x] = 1

chk = []
def dfs(v,chk=[]):
    chk.append(v)
    for w in range(len(edges[v])):
        # print(edges[v][w], w, chk)
        if edges[v][w] == 1 and w not in chk:
            dfs(w,chk)
    return len(chk) - 1
# for a in edges:
#     print(a)

print(dfs(1))