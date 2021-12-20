import sys
N = int(sys.stdin.readline())
wire = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
wire.sort()
dp = [0]*(N+1)

cross = [0] + [i[1] for i in wire]

for i in range(1,N+1):
    for j in range(i):
        if cross[i] > cross[j]:
            dp[i] = max(dp[i],dp[j]+1)
# print(cross)
# print(dp)

print(N-max(dp))
