import sys
N,M = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

left = 1
right = max(trees)

while(left <= right):
    H = (left + right) // 2
    wood = 0
    for i in trees:
        if i - H > 0:
            wood += i - H
    if wood >= M:
        left = H + 1
    else:
        right = H - 1

print(right)