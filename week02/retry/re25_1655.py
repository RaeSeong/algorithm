import sys
import heapq

N = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(N)]

leftheap = [-num[0]]
rightheap = []
middle = num[0]

print(middle)
for i in range(1,N):
    if num[i] < middle:
        heapq.heappush(leftheap, -num[i])
    else:
        heapq.heappush(rightheap, num[i])
    if len(leftheap) > len(rightheap) + 1:
        heapq.heappush(rightheap,-heapq.heappop(leftheap))
    elif len(rightheap) > len(leftheap):
        heapq.heappush(leftheap,-heapq.heappop(rightheap))
    middle = -leftheap[0]
    print(middle)