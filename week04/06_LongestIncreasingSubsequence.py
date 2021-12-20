import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
chk = [1]*(N)

for i in range(1,N):
    for j in range(i):
        if arr[i] > arr[j]:
            chk[i] = max(chk[i],chk[j] + 1)
    
print(max(chk))