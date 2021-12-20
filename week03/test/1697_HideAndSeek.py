import sys
from collections import deque as dq
N,K = map(int,sys.stdin.readline().split())

def subin(a,x):
    if a == 0:
        x -= 1
    elif a == 1:
        x += 1
    else:
        x *= 2
    return x

def catch():
    move = dq([])
    move.append(N)
    chk = [False]*(100001)
    repeat = len(move)
    cnt = 1
    while move:
        n = move.popleft()
        for i in range(3):
            X = subin(i,n)
            if X == K:
                return cnt
            if X > 100000 or X < 0 or chk[X]:
                continue
            move.append(X)
            chk[X] = True
        repeat -= 1
        if repeat > 0:
            continue
        repeat = len(move)
        cnt += 1

if N == K:
    print(0)
else:
    print(catch())