import sys
M,N,H = map(int,sys.stdin.readline().split())
tomato = []
for _ in range(H):
    tomato.append([list(map(int,sys.stdin.readline().split())) for _ in range(N)])

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
rippen = []
ptr = 0
end = 0

def ripe():
    tmp = 0
    global ptr
    global end
    for i in range(ptr,end):
        for j in range(6):
            X = rippen[i][0] + dx[j]
            Y = rippen[i][1] + dy[j]
            Z = rippen[i][2] + dz[j]
            if 0<=X<H and 0<=Y<N and 0<=Z<M and tomato[X][Y][Z] == 0:
                tomato[X][Y][Z] = 1
                rippen.append([X,Y,Z])
                tmp += 1
    ptr = end
    end += tmp

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                rippen.append([i,j,k])
                end += 1

result = 0
while ptr < end:
    ripe()
    result += 1

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0:
                print(-1)
                exit(0)
print(result-1)