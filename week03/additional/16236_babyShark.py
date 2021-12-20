import sys
from collections import deque as dq
N = int(sys.stdin.readline())
fish = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]

for i in range(N):
    for j in range(N):
        if fish[i][j] == 9:
            start = [[i,j]]
            fish[i][j] = 0
            
def yam(shark,feed):
    chk = [[False]*N for _ in range(N)]
    s,t = start.pop()
    queue = dq([[s,t]])
    chk[s][t] = True
    cnt = 1
    repeat = 1
    possible = []
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            X = x+dx[i]
            Y = y+dy[i]
            if 0 <= X < N and 0 <= Y < N and fish[X][Y] <= shark and not chk[X][Y]:
                chk[X][Y] = True
                if 0 < fish[X][Y] < shark:
                    possible.append([X,Y])
                    # fish[X][Y] = 0
                    # feed += 1
                    # if feed == shark:
                    #     shark += 1
                    #     feed = 0
                    # return [shark,feed,X,Y,cnt]
                queue.append([X,Y])
        repeat -= 1
        if repeat > 0:
            continue
        if len(possible) > 0:
            temp = []
            X = possible[0][0]
            for v in range(len(possible)):
                X = min(possible[v][0],X)
            for v in range(len(possible)):
                if possible[v][0] == X:
                    temp.append(possible[v][1])
            Y = min(temp)
            fish[X][Y] = 0
            feed += 1
            if feed == shark:
                shark += 1
                feed = 0
            return [shark,feed,X,Y,cnt]
        repeat = len(queue)
        cnt += 1
    
    return [shark,feed,X,Y,0]

a,b = 2,0
result = 0
while True:
    a,b,c,d,e = yam(a,b)
    # for i in fish:
    #     print(i)
    # print(a,b,c,d,e)
    if e == 0:
        break
    start.append([c,d])
    result += e
print(result)
