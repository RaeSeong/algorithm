import sys
N = int(sys.stdin.readline())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
num = []
[num.append(i[0]) for i in matrix]
num.append(matrix[N-1][1])
cnt = [[0]*(N) for _ in range(N)]

for i in range(1,N):
    for j in range(N-i):
        for k in range(i):
            cnt[j][j+i] = cnt[j][j+i],cnt[j-k][j+i-k]

for i in cnt:
    print(i)