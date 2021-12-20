import sys
cnt = int(sys.stdin.readline())
arr = [0]*10000
for i in range(cnt):
    arr[int(sys.stdin.readline())-1] += 1

for j in range(10000):
    for i in range(arr[j]):
        print(j+1)