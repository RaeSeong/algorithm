import sys
N = int(sys.stdin.readline())
triangle = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
maxval = [[0]*i for i in range(1,N+1)]
maxval[0][0] = triangle[0][0]

for i in range(1,N):
    for j in range(i+1):
        if j == 0:
            maxval[i][j] = maxval[i-1][j] + triangle[i][j]
        elif j == i:
            maxval[i][j] = maxval[i-1][j-1] + triangle[i][j]
        else:
            maxval[i][j] = max(maxval[i-1][j-1]+triangle[i][j],maxval[i-1][j]+triangle[i][j])

print(max(maxval[N-1]))