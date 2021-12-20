import sys
N = int(sys.stdin.readline())
stair = [int(sys.stdin.readline()) for _ in range(N)]
point = [0]*(N+1)
point[1] = stair[0]

for i in range(2,N+1):
    point[i] = max(point[i-2],point[i-3] + stair[i-2]) + stair[i-1]

# print(point)
print(point[N])