import sys
from collections import deque as dq
field = [list(sys.stdin.readline().rstrip()) for _ in range(12)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(12):
    for j in range(6):
        queue = dq([])
        chk = [[False]*6 for _ in range(12)]
        if field[11-i][j] != '.':
            color,I,J = field[11-i][j],11-i,j
            queue.append(color,I,J)
            chk[I,J] = True
            link = 1
            while queue:
                col,x,y = queue.popleft()
                for i in range(4):
                    X = x+dx[i]
                    Y = y+dy[i]
                    if 0 <= X < 12 and 0 <= Y < 6 and not chk[X,Y] and field[X][Y] == col:
                        chk[X][Y] = True
                        link += 1