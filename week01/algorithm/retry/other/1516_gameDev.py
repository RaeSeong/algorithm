import sys

N = int(sys.stdin.readline())
build = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
buildtime = [0]*N
leadtime = [0]*N
prebuildlist = [[] for _ in range(N)]

for i in range(N):
    build[i].pop()
    buildtime[i] += build[i][0]

for i in range(N):
    while(len(build[i]) > 1):
        prebuildlist[i].append(build[i].pop())


for i in range(N):
    for j in range(N):
        if len(prebuildlist[j]) == 0:
            fulfil = j
            prebuildlist[j].append('done')
            for k in prebuildlist:
                try:
                    del k[k.index(fulfil+1)]
                except:
                    continue
            break
    if i == 0:
        leadtime[fulfil] = buildtime[fulfil]
    else:
        leadtime[fulfil] = leadtime[last] + buildtime[fulfil]
    last = fulfil

print(leadtime)


