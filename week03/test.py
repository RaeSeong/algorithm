from collections import deque as dq
from collections import defaultdict as dd
edges = [[1,2],[1,5],[2,6],[2,3],[5,6],[3,4],[6,4],[4,7]]
queue = dq([])
graph = dd(list)
for i in edges:
    graph[i[0]].append(i[1])
graph = dict(graph)
indegree = [0]*(len(graph)+1)
for i in edges:
    indegree[i[1]-1] += 1

for i in range(1,len(indegree)):
    if indegree[i-1] == 0:
        queue.append(i)

align = []
while queue:
    a = queue.popleft()
    if a == 7:
        pass
    else:   
        for i in graph[a]:
            indegree[i-1] -= 1
            if indegree[i-1] == 0:
                queue.append(i)
        
        del graph[a]
    align.append(a)


print(graph,indegree)
print('i',queue)
print('align',align)