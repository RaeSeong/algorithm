import sys
from collections import deque as dq
R,C = map(int,sys.stdin.readline().split())
twmap = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
water = dq([])
hedgehog = dq([])
beaver = []
for i in range(R):
    for j in range(C):
        if twmap[i][j] == '*':
            water.append([i,j])
        elif twmap[i][j] == 'S':
            hedgehog.append([i,j])
            twmap[i][j] = 1
        elif twmap[i][j] == 'D':
            beaver.append([i,j])

cnt = len(water)

while hedgehog:
    try:
        a,b = water.popleft()
        for i in range(4):
            A = a+dx[i]
            B = b+dy[i]
            if 0 <= A < R and 0 <= B < C and twmap[A][B] == '.':
                twmap[A][B] = '*'
                water.append([A,B])
        cnt -= 1
        if cnt != 0:
            continue
        cnt = len(water)
    except:
        pass

    repeat = len(hedgehog)
    while repeat > 0:
        a,b = hedgehog.popleft()
        for i in range(4):
            A = a+dx[i]
            B = b+dy[i]
            if 0 <= A < R and 0 <= B < C and twmap[A][B] == '.':
                twmap[A][B] = twmap[a][b] + 1
                hedgehog.append([A,B])    
        repeat -= 1

    # for i in twmap:
    #     print(i)
    # print('-------------')

result = 10000
a,b = beaver.pop()
for i in range(4):
    A = a+dx[i]
    B = b+dy[i]
    try:
        if A >=0 and B >= 0:
            result = min(result,twmap[A][B])
    except:
        pass

if result == 10000:
    print('KAKTUS')
else:
    print(result)