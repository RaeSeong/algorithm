import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
assemble = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
toys = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
queue = [N]
midpart = set()
for i in assemble:
    toys[i[0]].append([i[1],i[2]])
    indegree[i[1]] += 1
    midpart.add(i[0])

result = [0]*(N+1)
result[N] = 1
while queue:
    a = queue.pop()
    for i in toys[a]:
        indegree[i[0]] -= 1
        result[i[0]] += result[a]*i[1]
        if indegree[i[0]] == 0:
            queue.append(i[0])

for i in range(1,N):
    if i not in midpart:
        print(i,result[i])
