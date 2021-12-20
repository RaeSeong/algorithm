import sys
N = int(sys.stdin.readline())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
cost = [[sum(max(matrix[i]) for i in range(N))]*(N+1) for _ in range(N)]
for i in cost:
    i[0] = 0

print(cost)
bit = [0]*N
for i in range(N):
    for j in range(1,N+1):
        for k in range(N-i):
            if matrix[k][i] == 0:
                continue
            cost[i][j] = min(cost[i][j],cost[k][j-1] + matrix[k][i])

print(cost)