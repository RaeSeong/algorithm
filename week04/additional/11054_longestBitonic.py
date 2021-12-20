import sys
N = int(sys.stdin.readline())
arr = [0] + list(map(int,sys.stdin.readline().split())) + [0]
inc = [0]*(N+2)
dec = [0]*(N+2)
for i in range(1,N+1):
    for j in range(i):
        if arr[i] > arr[j]:
            inc[i] = max(inc[i],inc[j]+1)
for i in range(N,0,-1):
    for j in range(N+1,i,-1):
        if arr[i] > arr[j]:
            dec[i] = max(dec[i],dec[j]+1)

# print(inc)
# print(dec)
result = 0
for i in range(N+1):
    result = max(result,inc[i]+dec[i]-1)


print(result)