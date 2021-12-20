import sys
import heapq
N,K = map(int,sys.stdin.readline().split())
gem = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
bag = [int(sys.stdin.readline()) for _ in range(K)]
bag.sort()
heap = []
for i in bag:
    
    heapq.heappush(heap,gem[0][1])
    heapq.heappop(gem)
