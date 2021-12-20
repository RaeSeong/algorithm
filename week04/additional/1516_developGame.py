import sys
N = int(sys.stdin.readline())
tech = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
# for i in tech:
#     i[1:len(i)-1].sort(reverse=True)
# tech.sort(key=lambda x:x[1:len(x)-1])
# print(tech)
a,b = [tech[i][0] for i in range(N)],[tech[i][1:len(tech[i])-1] for i in range(N)]
indegree = [0]*N
graph = [[] for _ in range(N)]
for i in range(N):
    for j in b[i]:
        graph[j-1].append(i)
# print(graph)
for i in range(N):
    indegree[i] = len(b[i])
# print(indegree)
queue = []
order = []
for i in range(N):
    if indegree[i] == 0:
        queue.append(i)
        indegree[i] -= 1
        order.append(i)

while queue:
    c = queue.pop()
    for i in graph[c]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)
            indegree[i] -= 1
            order.append(i)

# print(indegree)
# print(a,b)
# print('order',order)
build = [0]*N
build[0] = tech[0][0]
techsort = [[] for _ in range(N)]
for i in range(N):
    techsort[order[i]] = tech[i]
# print(techsort)
for i in range(N):
    need = len(tech[i]) - 2
    if need == 0:
        build[i] = tech[i][0]
    for j in range(1,need+1):
        build[i] = max(build[i],build[tech[i][j]-1] + tech[i][0])

for i in build:
    print(i)


