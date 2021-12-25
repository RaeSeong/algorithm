import sys
N = int(sys.stdin.readline())
if N == 1 or N == 2:
    print(1)
    exit(0)
arr = [0]*N
arr[0] = 1
arr[1] = 1

for i in range(N-2):
    arr[i+2] = arr[i+1] + arr[i]

print(arr[N-1])