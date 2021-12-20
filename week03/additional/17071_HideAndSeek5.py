#시간초과
import sys
from collections import deque as dq
N,K = map(int,sys.stdin.readline().split())

def catch():
    cnt = 1
    queue = dq([N])
    repeat = 1
    young = K+1
    move = 1
    while queue:
        subin = queue.popleft()
        for i in range(3):
            X = chase(subin,i)
            if X > 500000 or X < 0:
                continue
            if young == X:
                return cnt
            queue.append(X)
        repeat -= 1
        if repeat > 0:
            continue
        repeat = len(queue)
        cnt += 1
        move += 1
        young += move
        if young > 500000:
            return -1



def chase(x,a):
    if a == 0:
        x *= 2
    elif a == 1:
        x += 1
    else:
        x -= 1
    return x

if K == N:
    print(0)
else:
    print(catch())