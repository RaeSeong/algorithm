import sys
from collections import defaultdict as dd
from collections import deque as dq
N,M = map(int,sys.stdin.readline().split())
heavier = dd(list)
lighter = dd(list)
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    heavier[a].append(b)
    lighter[b].append(a)
heavier = dict(heavier)
lighter = dict(lighter)


chk = []
queue = dq([])
def bfs(v,a):
    queue.append(v)
    cnt = 0
    while queue:
        V = queue.popleft()
        cnt += 1
        if V not in keys:
            continue
        for i in a[V]:
            if i not in chk:
                chk.append(i)
                queue.append(i)
    return cnt - 1    

result = 0
keys = [i for i in heavier]
for j in heavier:
    side = bfs(j,heavier)
    if side > N//2:
        result += 1
    chk = []
keys = [i for i in lighter]
for k in lighter:
    side = bfs(k,lighter)
    if side > N//2:
        result += 1
    chk = []

print(result)