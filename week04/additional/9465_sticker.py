import sys
T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    sticker = [[0,0] + list(map(int,sys.stdin.readline().split())) for _ in range(2)]
    val = [[0]*(N+2) for _ in range(2)]

    for i in range(2,N+2):
        for j in range(2):
            val[j][i] = max(val[1-j][i-2],val[1-j][i-1]) + sticker[j][i]

    print(max(val[0][N+1],val[1][N+1]))