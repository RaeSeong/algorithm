import sys
R,C = map(int,sys.stdin.readline().split())
board = [sys.stdin.readline().rstrip() for _ in range(R)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
result = 1

def dfs(x,y,chk):
    global result
    cnt = 0
    for i in range(4):
        X = x+dx[i]
        Y = y+dy[i]
        if 0 <= X < R and 0 <= Y < C and board[X][Y] not in chk:
            dfs(X,Y,chk+board[X][Y])
        else:
            cnt += 1
    if cnt == 4:
        result = max(result,len(chk))


dfs(0,0,board[0][0])
print(result)
