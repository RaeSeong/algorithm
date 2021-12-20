import sys
N = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
chk = [[0]*N for _ in range(N)]

def dfs(x,y):
    if x == N-1 and y == N-1:
        return 1
    if board[x][y] == 0:
        return 0
    if chk[x][y] > 0:
        return chk[x][y]
    v = board[x][y]
    for i in range(2):
        X = x+v*(1-i)
        Y = y+v*i
        if X < N and Y < N:
            chk[x][y] += dfs(X,Y)
    return chk[x][y]

print(dfs(0,0))
# for i in chk:
#     print(i)
