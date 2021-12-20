import sys
N = int(sys.stdin.readline())
apple = int(sys.stdin.readline())
loc = []
for i in range(apple):
    loc.append(list(map(int,sys.stdin.readline().split())))
cmd = int(sys.stdin.readline())
do = []
for j in range(cmd):
    do.append(list(sys.stdin.readline().split()))
headX, headY = 0
tail = []
# for i in range(N):
#     tail.append([False]*N)

direction = 0
while True:
    if direction == 0:
        headY += 1
    elif direction == 1:
        headX += 1
    elif direction == 2:
        headY -= 1
    else:
        headX -= 1