import sys
from collections import deque
R,C = map(int,sys.stdin.readline().split())
twmap = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
# beaver = []
water = deque([])
# stone = []
hedge = deque([])

for i in range(R):
    for j in range(C):
        # if twmap[i][j] == 'D':
        #     beaver = [i,j]
        if twmap[i][j] == 'S':
            hedge.append([i,j])
        elif twmap[i][j] == '*':
            twmap[i][j] = 0
            water.append([i,j])
        # elif twmap[i][j] == 'X':
        #     stone.append([i,j])

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def flood():
    waterturn = len(water)
    while water:
        if waterturn == 0:
            waterturn = len(water)
        a,b = water.popleft()
        for i in range(4):
            A = a + dx[i]
            B = b + dy[i]
            if 0<=A<R and 0<=B<C and twmap[A][B] == '.':
                twmap[A][B] = twmap[a][b] + 1
                water.append([A,B])
        waterturn -= 1

def escape():
    hedgeturn = 1
    cnt = 1
    while hedge:
        if hedgeturn == 0:
            hedgeturn = len(hedge)
            cnt += 1
        a,b = hedge.popleft()
        for i in range(4):
            A = a + dx[i]
            B = b + dy[i]
            if 0<=A<R and 0<=B<C:
                if twmap[A][B] == 'D':
                    return cnt
                elif twmap[A][B] == '.':
                    hedge.append([A,B])
                elif twmap[A][B] != 'S' and twmap[A][B] != 'X' and twmap[A][B] > cnt:
                    hedge.append([A,B])
        hedgeturn -= 1
    return 'KAKTUS'

flood()

print(escape())