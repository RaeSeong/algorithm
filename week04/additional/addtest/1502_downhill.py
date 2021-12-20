import sys
sys.setrecursionlimit(10**8)
N,M = map(int,sys.stdin.readline().split())
roadmap = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
chk = [[-1]*M for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    # for i in chk:
    #     print(i)
    # print('---------')
    if x == N-1 and y == M-1:
        return 1
    if chk[x][y] >= 0:
        return chk[x][y]
    chk[x][y] = 0
    for i in range(4):
        X = x+dx[i]
        Y = y+dy[i]
        if 0 <= X < N and 0 <= Y < M:
            if roadmap[X][Y] < roadmap[x][y]:
                chk[x][y] += dfs(X,Y)
    # for i in chk:
    #     print(i)
    # print('-------------')
    return chk[x][y]


# for i in chk:
#     print(i)
print(dfs(0,0))