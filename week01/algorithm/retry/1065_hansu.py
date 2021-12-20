import sys
N = int(sys.stdin.readline())
result = 0
if N < 100:
    result = N
else:
    result = 99
    count = 0
    for j in range(100,N+1):
        arr = list(map(int,str(j)))
        diff = arr[0] - arr[1]
        for i in range(1,len(arr)-1):
            if diff != arr[i] - arr[i+1]:
                count -= 1
                break
        count += 1
    result += count

print(result)