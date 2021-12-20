import sys
N = int(sys.stdin.readline())
bundle = [N+1]*(N+1)
bundle[0] = 0
bundle[3] = 1
for n in range(5,N+1):
    bundle[n] = min(bundle[n-3]+1,bundle[n-5]+1)

if bundle[N] > N:
    print(-1)
else:
    print(bundle[N])