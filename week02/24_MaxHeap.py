
import heapq
import sys
from collections import deque
N = int(sys.stdin.readline())
arr = []
queue = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

for j in range(N):
    if arr[j] > 0:
        heapq.heappush(queue,-arr[j])
    else:
        if len(queue) == 0:
            print(0)
        else:
            print(-heapq.heappop(queue))