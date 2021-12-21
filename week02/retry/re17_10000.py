import sys
N = int(sys.stdin.readline())
circles = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

area = []
for i in circles:
    area.append([i[0]-i[1], i[0]+i[1]])

area.sort(key = lambda x:(x[0],-x[1]))

print(area)