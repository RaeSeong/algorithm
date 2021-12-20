import sys
from collections import deque
N,K = map(int,sys.stdin.readline().split())
num = deque(list(map(int,sys.stdin.readline().rstrip())))

while True:
    a = num.popleft()
    b = num.popleft()
    
    if a > b:
        num.appendleft(a)
    else:
        num.appendleft(b)
    break

print(num)