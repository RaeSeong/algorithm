import sys
n,k = map(int,sys.stdin.readline().split())
coin = {int(sys.stdin.readline()) for _ in range(n)}
coin = list(coin)
coin.sort()
K = k + 1
won = [K for _ in range(K)]
won[0] = 0

for i in coin:
    for j in range(i,K):
        won[j] = min(won[j],won[j-i]+1)

if won[k] == K:
    print(-1)
else:
    print(won[k])