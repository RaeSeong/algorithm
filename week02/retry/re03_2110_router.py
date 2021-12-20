import sys
N,C = map(int,sys.stdin.readline().split())
houses = [int(sys.stdin.readline()) for _ in range(N)]
houses.sort()

start = houses[0]
end = houses[-1] - houses[0]
answer = 0

while(start <= end):
    mid = (start+end)//2
    route = 1
    distance = 0
    for i in range(N-1):
        distance += houses[i+1] - houses[i]
        if distance >= mid:
            route += 1
            distance = 0

    if route >= C:
        start = mid +1
        answer = mid
    else:
        end = mid -1

print(answer)
