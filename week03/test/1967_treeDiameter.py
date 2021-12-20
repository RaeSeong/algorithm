import sys
N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
edges = [list(map(int,sys.stdin.readline().split())) for _ in range(N-1)]

for i in edges:
    tree[i[0]].append([i[1],i[2]])
    tree[i[1]].append([i[0],i[2]])

for i in tree:
    print(i)