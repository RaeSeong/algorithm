import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
assemble = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
toys = [[] for _ in range(N+1)]
for i in assemble:
    toys[i[0]].append([i[1],i[2]])

# for i in toys:
#     print(i)
ans = [0,0,0,0,0]
while toys[N]:
    a,b = toys[N].pop()
    if a < 5:
        ans[a] += b
    else:
        for i in toys[a]:
            x,y = i
            toys[N].append([x,y*b])

for i in range(1,5):
    if ans[i] > 0:
        print(i,ans[i])

##############################################
import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
assemble = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
toys = [[] for _ in range(N+1)]
for i in assemble:
    toys[i[0]].append([i[1],i[2]])

dp = []
for i in range(N+1):
    if len(toys[i]) == 0:
        dp.append(i)

ans = [0 for _ in range(max(dp)+1)]

while toys[N]:
    a,b = toys[N].pop()
    if a in dp:
        ans[a] += b
    else:
        for i in toys[a]:
            x,y = i
            toys[N].append([x,y*b])

for i in range(1,max(dp)+1):
    if ans[i] > 0:
        print(i,ans[i])