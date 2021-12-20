import sys
N = int(sys.stdin.readline())
cft = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
cft.sort(key = lambda x:(x[1],x[0]))
last = 0
cnt = 0
for i in cft:
    if i[1] >= last and i[0] >= last:
        last = i[1]
        cnt += 1

print(cnt)
