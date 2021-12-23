import sys
from collections import deque
N = int(sys.stdin.readline())
edge = [list(map(int,sys.stdin.readline().split())) for _ in range(N-1)]
tree = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

for i in edge:
    tree[i[0]].append(i[1])
    tree[i[1]].append(i[0])

queue = deque([])

def bfs():
    while queue:
        node = queue.popleft()
        while tree[node]:
            i = tree[node].pop()
            queue.append(i)
            if i > 1 and parent[i] == 0:
                parent[i] = node

queue.append(1)

bfs()
for i in range(2,N+1):
    print(parent[i])