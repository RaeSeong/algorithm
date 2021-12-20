import sys
N,M = map(int,sys.stdin.readline().split())
pd = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
singer = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for i in pd:
    for j in range(1,len(i)-1):
        singer[i[j]].append(i[j+1])
        indegree[i[j+1]] += 1


queue = []
result = []
for i in range(1,N+1):
    if indegree[i] == 0:
        indegree[i] -= 1
        queue.append(i)
        result.append(i)
# print(queue)
# print(singer)
while queue:
    a = queue.pop()
    for i in singer[a]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)
            result.append(i)


# print(pd)
# print(indegree)
# print(singer)
if len(result) == N:
    for i in result:
        print(i)
else:
    print(0)