import sys
from collections import deque
N = int(sys.stdin.readline())
towers = list(map(int,sys.stdin.readline().split()))
chktower = []
getsignal = 0
result = ['0']
for i in range(len(towers)-1):
    chktower.append([i,towers[i]])
    while True:
        # if len(chktower) == 0:
        #     getsignal = 0
        #     break
        try:
            a = chktower.pop()
            if a[1] > towers[i+1]:
                getsignal = a[0]+1
                chktower.append(a)
                break
        except:
            chktower.append([i+1,towers[i+1]])
            getsignal = 0
            break
    result.append(str(getsignal))
resultstr = " ".join(result)
print(resultstr)

#over time
# result = ''
# for i in range(len(towers)):
#     deq = deque(towers[0:i+1])
#     if len(deq) == 1:
#         if len(towers) > 1:
#             result += '0 '
#         else:
#             result += '0'
#         continue
#     sign = deq.pop()
#     while True:
#         accept = deq.pop()
#         if accept >= sign:
#             result += str(len(deq)+1)
#             break
#         if len(deq) == 0:
#             result += '0'
#             break
#     result += ' '
    
# print(result)