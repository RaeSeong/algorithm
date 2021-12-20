import sys
sys.setrecursionlimit(10**8)
N,M = map(int,sys.stdin.readline().split())
maap = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
move = [[-1]*M for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    if x == N-1 and y == M-1:
        return 1
    if move[x][y] >= 0:
        return move[x][y]
    move[x][y] = 0
    for i in range(4):
        X = x+dx[i]
        Y = y+dy[i]
        if 0 <= X < N and 0 <= Y < M and maap[x][y] > maap[X][Y]:
            move[x][y] += dfs(X,Y)
    return move[x][y]


print(dfs(0,0))
