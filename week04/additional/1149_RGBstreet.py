import sys
N = int(sys.stdin.readline())
rgb = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
cost = [[0]*3 for _ in range(N)]
cost[0] = rgb[0]

for i in range(1,N):
    for j in range(3):
        cost[i][j] = min(cost[i-1][j-2] + rgb[i][j],cost[i-1][j-1] + rgb[i][j])

print(min(cost[N-1]))
    