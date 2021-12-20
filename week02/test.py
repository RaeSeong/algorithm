#가장 긴 증가하는 부분수열 
# while 안에 while 변수를 수정하면 바깥 while 변수에도 영향을 미치네?
import sys
from collections import deque
N = int(sys.stdin.readline())
arr = map(int,sys.stdin.readline().split())
dq = deque(arr)
retry = deque([])
compare = 0
long = 0
max = 0
while True:
    while True:
        print(dq)
        chk = deque.popleft(dq)
        print(chk)
        print(dq)
        if compare >= chk:
            print('?',dq)
            deque.append(retry,chk)
            print('if',dq)
        else:
            compare = chk
            long += 1
            print('else',dq)
        print(dq,len(dq))
        if len(dq) == 0:
            if long > max:
                max = long
            long = 0
            break
    print(retry,max)
    if len(retry) < max:
        break
    dq = retry
    compare = 0

print(max)