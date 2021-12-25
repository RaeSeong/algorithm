import sys
N,K = map(int,sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(N)]

now = 0
for i in range(N):
    if coin[i] > K:
        now = i-1
        break

cnt = 0

while K > 0 and now >= 0:
    if K >= coin[now]:
        cnt += K//coin[now]
        K -= (K//coin[now]) * coin[now]
    now -= 1

print(cnt)