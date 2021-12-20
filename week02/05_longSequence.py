import sys
from collections import deque
N = int(sys.stdin.readline())
arr = map(int,sys.stdin.readline().split())


# dq = deque(arr)
# dq1 = deque([])
# retry = False
# compare = 0
# long = 0
# max = 0
# while True:
#     while True:
#         chk = deque.popleft(dq)
#         if compare >= chk:
#             if retry == False:
#                 retry = True
#         else:
#             compare = chk
#             long += 1
#         if retry == True:
#             dq1.append(chk)
#         if len(dq) == 0:
#             if long > max:
#                 max = long
#             long = 0
#             break
#         # cnt += 1

#     for i in range(len(dq1)):
#         dq.append(deque.popleft(dq1))

#     if len(dq) - 1 < max:
#         break

#     compare = 0
#     retry = False

# print(max)