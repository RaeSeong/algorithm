import sys
arr = []
while True:
    imsi = list(map(int,sys.stdin.readline().split()))
    if imsi[0] == 0:
        break
    arr.append(imsi)

print(arr)
