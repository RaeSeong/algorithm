import sys
N,K = map(int,sys.stdin.readline().split())
stuff = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
val = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        if stuff[i-1][0] <= j:
            val[i][j] = max(val[i-1][j], val[i-1][j - stuff[i-1][0]] + stuff[i-1][1])
        else:
            val[i][j] = val[i-1][j]

print(val[N][K])