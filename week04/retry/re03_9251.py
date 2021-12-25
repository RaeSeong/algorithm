import sys
first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()

arr = [0 for _ in range(len(first))]
for i in range(len(second)):
    cnt = 0
    for j in range(len(first)):
        if cnt < arr[j]:
            cnt = arr[j]
        elif second[i] == first[j]:
            arr[j] = cnt + 1

print(max(arr))