import sys
N = int(sys.stdin.readline())
arr = [float('inf')] + list(map(int,sys.stdin.readline().split()))
dec = [0]*(N+1)
for i in range(1,N+1):
    for j in range(i):
        if arr[i] < arr[j]:
            dec[i] = max(dec[i],dec[j]+1)

print(max(dec))


