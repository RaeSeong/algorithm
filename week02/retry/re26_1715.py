import sys
import heapq
N = int(sys.stdin.readline())
card = []
for _ in range(N):
    heapq.heappush(card, int(sys.stdin.readline()))

result = 0

while len(card) > 1:
    compareCnt = heapq.heappop(card) + heapq.heappop(card)
    result += compareCnt
    heapq.heappush(card, compareCnt)

print(result)