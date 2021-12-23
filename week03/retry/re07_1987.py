import sys
R,C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline()) for _ in range(R)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

result = 0
def dfs(x,y,alpha):
    print(alpha)
    global result
    result = max(result, len(alpha))
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if 0<=X<R and 0<=Y<C and board[X][Y] not in alpha:
            alpha.add(board[X][Y])
            dfs(X,Y,alpha)
            alpha.remove(board[X][Y])

#     return len(alpha)

# result = 
dfs(0,0,set(board[0][0]))
print(result)
