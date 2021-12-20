import sys
from collections import deque as dq
M,N,H = map(int,sys.stdin.readline().split())
store = [[list(map(int,sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
dx = [0,0,0,0,-1,1]
dy = [0,1,0,-1,0,0]
dz = [1,0,-1,0,0,0]
queue = dq([])
for i in range(H):
    for j in range(N):
        for k in range(M):
            if store[i][j][k] == 1:
                queue.append([i,j,k])


def ripe():
    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            X = x+dx[i]
            Y = y+dy[i]
            Z = z+dz[i]
            if 0 <= X < H and 0 <= Y < N and 0 <= Z < M and store[X][Y][Z] == 0:
                queue.append([X,Y,Z])
                store[X][Y][Z] = store[x][y][z] + 1

ripe()
day = 0
result = 0
unripe = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if store[i][j][k] == 0:
                unripe = True
            else:
                day = max(store[i][j][k],day)

if unripe:
    result = -1
else:
    result = day - 1

print(result)