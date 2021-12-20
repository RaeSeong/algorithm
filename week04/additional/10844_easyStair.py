import sys
N = int(sys.stdin.readline())
arr = [0]*(N+3)
arr[1] = 9
arr[2] = 17
for i in range(3,N+1):
    arr[i] = ((arr[i-1]-1)*2)%(10**9)

print(arr[N])