import sys
from collections import deque as dq
N,M = map(int,sys.stdin.readline().split())
maze = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
chk = []
queue = dq([])
road = [[0]*M for _ in range(N)]
road[0][0] = 1
queue.append([0,0])
while queue:
    x,y = queue.popleft()
    if x == N-1 and y == M-1:
        break
    for i in range(4):
        X = x+dx[i]
        Y = y+dy[i]
        if 0 <= X < N and 0 <= Y < M and [X,Y] not in chk and maze[X][Y] == '1':
            chk.append([X,Y])
            queue.append([X,Y])
            road[X][Y] = road[x][y] + 1
print(road[N-1][M-1])
# for i in road:
#     print(i)
