import sys
N,K = map(int,sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(N)]

cnt = 0
while K > 0:
    a = coin.pop()
    b = K//a
    if b > 0:
        K = K - a*b
    cnt += b

print(cnt)
