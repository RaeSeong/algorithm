import sys
N,K = map(int,sys.stdin.readline().split())
item = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
val = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        if item[i-1][0] > j:
            val[i][j] = val[i-1][j]
        else:
            val[i][j] = max(val[i-1][j-item[i-1][0]]+item[i-1][1],val[i-1][j])

# for i in val:
#     print(i)
print(val[N][K])
    