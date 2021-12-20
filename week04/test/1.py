import sys
N = int(sys.stdin.readline())
step = [0] + [int(sys.stdin.readline()) for _ in range(N)]
point = [0]*(N+1)
for i in range(1,N+1):
    if i < 3:
        point[i] = point[i-1] + step[i]
        continue
    point[i] = max(point[i-3]+step[i-1],point[i-2]) + step[i]

print(point[N])