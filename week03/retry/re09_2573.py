import sys
from collections import deque
N,M = map(int, sys.stdin.readline().split())
iceberg = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
tmp = [list(i) for i in iceberg]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
icequeue = deque([])
fail = False

def chk():
    global fail
    fail = True
    chk = [[False]*M for _ in range(N)]
    startice = 0
    for i in range(1,N-1):
        for j in range(1,M-1):
            if iceberg[i][j] > 0:
                icequeue.append([i,j])
                startice = i
                break
        if icequeue:
            break

    while icequeue:
        x,y = icequeue.popleft()
        chk[x][y] = True
        melt(x,y)
        for i in range(4):
            X = x+dx[i]
            Y = y+dy[i]
            if 1<=X<N-1 and 1<=Y<M-1 and iceberg[X][Y] > 0 and not chk[X][Y]:
                # melt(X,Y)
                chk[X][Y] = True
                icequeue.append([X,Y])

    for i in range(startice,N-1):
        for j in range(1,M-1):
            if iceberg[i][j] > 0:
                if not chk[i][j]:
                    return False
                else:
                    fail = False

    return True

def melt(x,y):
    for i in range(4):
        X = x+dx[i]
        Y = y+dy[i]
        if iceberg[X][Y] == 0 and tmp[x][y] > 0:
            tmp[x][y] -= 1


one = True
year = -1
while one:
    one = chk()
    if fail:
        print(0)
        exit(0)
    year += 1
    iceberg = [list(i) for i in tmp]

print(year)

