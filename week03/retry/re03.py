import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
# maze = list(sys.stdin.readline().strip())
maze = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

mapchk = [[0]*M for _ in range(N)]

def course():
    queue = deque([])
    queue.append([0,0])
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            A = a+dy[i]
            B = b+dx[i]
            if 0 <= A < N and 0 <= B < M and maze[A][B] == 1 and mapchk[A][B] == 0:
                mapchk[A][B] = mapchk[a][b] + 1
                queue.append([A,B])

mapchk[0][0] = 1
course()
print(mapchk[N-1][M-1])