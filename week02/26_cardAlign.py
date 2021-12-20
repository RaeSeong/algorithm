import sys
import heapq
N = int(sys.stdin.readline())
cards = []
for i in range(N):
    value = int(sys.stdin.readline())
    heapq.heappush(cards, value)

result = 0
for i in range(N-1):
    push = heapq.heappop(cards) + heapq.heappop(cards)
    result += push
    heapq.heappush(cards,push)

print(result)