import sys
# from collections import deque
N,M = map(int,sys.stdin.readline().split())
edges = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]
queue = []#deque([])
indegree = [0]*(N+1)
for i in edges:
    graph[i[0]].append(i[1])
    indegree[i[1]] += 1

result = []

for i in range(1,N+1):
    if indegree[i] == 0:
        queue.append(i)
        indegree[i] -= 1
        result.append(i)

while queue:
    a = queue.pop()#popleft()
    for i in graph[a]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)
            result.append(i)

print(*result)