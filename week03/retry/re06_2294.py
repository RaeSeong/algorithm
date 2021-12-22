import sys
from collections import deque
n,k = map(int,sys.stdin.readline().split())
coin = set()
for _ in range(n):
    coin.add(int(sys.stdin.readline()))
coin = list(coin)
coin.sort()

won = [float('inf') for _ in range(k+1)]
won[0] = 0

for i in coin:
    for j in range(i,k+1):
        won[j] = min(won[j-i]+1,won[j])

if won[k] == float('inf'):
    print(-1)
else:
    print(won[k])
    

#################################################################

# queue = deque([])

# def won():
#     while queue:
#         value, cnt = queue.popleft()
#         if value == k:
#             return cnt
#         elif value < k:
#             for i in coin:
#                 queue.append([value+i, cnt+1])

# for i in coin:
#     queue.append([i,1])

# print(won())

##################################################################

# possible = []

# def won(a,cnt):
#     if a > k:
#         return
#     if a == k:
#         possible.append(cnt)
#     for i in coin:
#         won(a+i,cnt+1)

# for i in coin:
#     won(i,1)

# print(possible)