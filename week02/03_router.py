import sys
N,C = map(int,sys.stdin.readline().split())
houses = []
for i in range(N):
    houses.append(int(sys.stdin.readline()))
houses.sort()
cnt = 1
left = 1
right = houses[-1] - houses[0]
while left <= right:
    mid = (left + right) // 2
    put = 0
    for i in range(len(houses)-1):
        put += houses[i+1] - houses[i]
        if put >= mid:
            cnt += 1
            put = 0
        if cnt > C:
            global answer
            left = mid + 1
            answer = mid
            break
    if C > cnt:
        right = mid - 1
        cnt = 1
print(answer)