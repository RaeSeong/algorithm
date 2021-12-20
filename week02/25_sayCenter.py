import sys
import heapq
N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

maxheap = []
minheap = []

for i in arr:
    heapq.heappush(maxheap,-i)
    heapq.heappush(minheap,i)
    maxlist = list(maxheap)
    minlist = list(minheap)
    while True:
        a = -heapq.heappop(maxlist)
        b = heapq.heappop(minlist)
        if a <= b:
            print(a)
            break
