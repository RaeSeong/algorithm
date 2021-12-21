import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
apple = [list(map(int,sys.stdin.readline().split())) for _ in range(K)]
L = int(sys.stdin.readline())
command = [list(sys.stdin.readline().split()) for _ in range(K)]

dummy = [[0]*N for _ in range(N)]
head = [0,0]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
direction = 0
sec = 0
while True:
    if 0 <= head[0] < N and 0 <= head[1] < N and dummy[head[0]][head[1]] == 0:
        head[0] += dy[direction]
        head[1] += dx[direction]
        if [head[0],head[1]] in apple:
            apple.remove([head[0],head[1]])
        