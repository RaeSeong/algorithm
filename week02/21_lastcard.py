import sys
from collections import deque
N = int(sys.stdin.readline())
cards = []
for i in range(N):
    cards.append(i+1)

deq = deque(cards)

while True:
    if len(deq) == 1:
        print(deq.pop())
        break
    deq.popleft()
    deq.rotate(-1)

    
    



# def cardleave(num,cnt,leave,rest):
#     distance = cnt*2
#     if num < 2**cnt:
#         print(leave)
#         return
#     if num%2 == 0:
#         leave = distance - rest
#     else:
#         leave = distance - 2**(cnt-1) - rest
#     cnt += 1
#     rest += 2**(cnt-1)
#     cardleave(num,cnt,leave,rest)

# cardleave(N,1,1,0)