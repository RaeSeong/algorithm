import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
sea = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
meltsea = list(map(list,sea))
water = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
chk = [[False]*M for _ in range(N)]
def melt(x,y):
    for i in range(4):
        if meltsea[x][y] == 0:
            return
        X = x+dx[i]
        Y = y+dy[i]
        if sea[X][Y] == 0:
            meltsea[x][y] -= 1
            if meltsea[x][y] == 0:
                water.append([x,y])

queue = deque([])
def seprate():
    if not water:
        return False
    a,b = water.pop()
    queue.append([a,b])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            X = x+dx[i]
            Y = y+dy[i]
            if meltsea[X][Y] == 0 or chk[X][Y] == True:
                continue
            chk[X][Y] = True
            queue.append([X,Y])
    water.append([a,b])
    while water:    
        a,b = water.pop()
        for i in range(4):
            A = a+dx[i]
            B = b+dy[i]
            if meltsea[A][B] != 0 and chk[A][B] == False:
                return True
    return False

year = 1
while True:
    allsum = 0
    for i in sea:
        allsum += sum(i)
    if allsum == 0:
        print(0)
        break
    for i in range(1,N-1):
        for j in range(1,M-1):
            melt(i,j)
    # for i in range(N):
    #     print(sea[i])
    # print('--------------------')
    # for i in range(N):
    #     print(meltsea[i])
    result = seprate()
    # for i in chk:
    #     print(i)

    if result == True:
        print(year)
        break
    water = []
    sea = list(map(list,meltsea))
    chk = [[False]*M for _ in range(N)]
    year += 1