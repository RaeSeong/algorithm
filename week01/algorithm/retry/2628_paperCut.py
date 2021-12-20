import sys

horizon, vertical = map(int,sys.stdin.readline().split())
N = int(sys.stdin.readline())
cut = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

seperate_horizon = []
seperate_vertical = []
for i in cut:
    if i[0] == 0:
        seperate_vertical.append(i[1])
    else:
        seperate_horizon.append(i[1])

seperate_horizon.extend([0,horizon])
seperate_vertical.extend([0,vertical])

seperate_vertical.sort()
seperate_horizon.sort()

max_horizon = 0
for i in range(1,len(seperate_horizon)):
    if seperate_horizon[i] - seperate_horizon[i-1] > max_horizon:
        max_horizon = seperate_horizon[i] - seperate_horizon[i-1]

max_vertical = 0
for i in range(1,len(seperate_vertical)):
    if seperate_vertical[i] - seperate_vertical[i-1] > max_vertical:
        max_vertical = seperate_vertical[i] - seperate_vertical[i-1]
    
print(max_vertical * max_horizon)