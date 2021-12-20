import sys
T = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(T)]
for N in arr:
    dp = [0]*N
    if N == 1:
        dp[0] = 1
    elif N == 2:
        dp[0],dp[1] = 1,1
    elif N == 3:
        dp[0],dp[1],dp[2] = 1,1,1
    else:
        dp[0],dp[1],dp[2],dp[3] = 1,1,1,2
    
    for i in range(4,N):
        dp[i] = dp[i-1]+dp[i-5]
    print(dp[N-1])