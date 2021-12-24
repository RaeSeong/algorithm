import sys
from collections import deque
N = int(sys.stdin.readline())
tech = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
sec = [0]*(N+1)
connection = [[] for _ in range(N+1)]
indgr = [0]*(N+1)
time = [[0]*(N+1) for _ in range(N+1)]

queue = []
for idx,build in enumerate(tech):
    for cnt,dev in enumerate(build):
        if cnt > 0 and dev != -1:
            connection[dev].append([idx+1, val])
            indgr[idx+1] += 1
        elif cnt == 0:
            val = dev
        elif cnt == 1:
            queue.append([idx+1,val])


while queue:
    idx, val = queue.pop()
    time[idx][idx] = max(time[idx])+val
    for a, b in connection[idx]:
        time[a][idx] = time[idx][idx]
        indgr[a] -= 1
        if indgr[a] == 0:
            queue.append([a,b])

for i in range(1,N+1):
    print(time[i][i])