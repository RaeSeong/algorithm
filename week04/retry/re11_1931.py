import sys
N = int(sys.stdin.readline())
confer = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
confer.sort(key = lambda x: (x[1],x[0]))

result = 0
now = [0,0]
for i in confer:
    if i[0] >= now[1]:
        now = i
        result += 1

print(result)