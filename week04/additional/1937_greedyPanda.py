import sys
N = int(sys.stdin.readline())
forest = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
bamboo = [[0]*N for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(N):
    for j in range(N):
        for k in range(4):
            I = i+dx[k]
            J = j+dy[k]
            if 0 <= I < N and 0 <= J < N and forest[i][j] < forest[I][J]:
                bamboo[i][j] = max(bamboo[i][j],bamboo[I][J]+1)

for i in bamboo:
    print(i)