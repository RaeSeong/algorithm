import sys
from collections import deque as dq
N = int(sys.stdin.readline())
apt = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
danji = []

chk = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if apt[i][j] == 1 and not chk[i][j]:
            queue = dq([])
            queue.append([i,j])
            chk[i][j] = True
            cnt = 1
            while queue:
                x,y = queue.popleft()
                for k in range(4):
                    X = x+dx[k]
                    Y = y+dy[k]
                    if 0 <= X < N and 0 <= Y < N and apt[X][Y] == 1 and not chk[X][Y]:
                        chk[X][Y] = True
                        queue.append([X,Y])
                        cnt += 1
            danji.append(cnt)

print(len(danji))
danji.sort()
for i in danji:
    print(i)