import sys
N = int(sys.stdin.readline())
W = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
route = []

def TSP(now, city, cost):
    if len(city) == N + 1 and now == city[0]:
        route.append(cost)
        return
    for i in range(N):
        if W[now][i] != 0 and (i not in city or (len(city) == N and i == city[0])):
            city.append(i)
            TSP(i,city,cost + W[now][i])
            city.remove(i)
    

for i in range(N):
    TSP(0,[i],0)

print(min(route))