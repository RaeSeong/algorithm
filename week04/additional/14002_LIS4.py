import sys
N = int(sys.stdin.readline())
arr = [0] + list(map(int,sys.stdin.readline().split()))
inc = [0]*(N+1)
val = [[] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(i):
        if arr[i] > arr[j]:
            if inc[i] < inc[j] + 1:
                inc[i] = inc[j] + 1
                val[i] = val[j] + [arr[i]]

print(max(inc))
print(*val[inc.index(max(inc))])