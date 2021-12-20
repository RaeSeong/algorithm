import sys
N = int(sys.stdin.readline())
area = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
chk = [[False]*N for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def rain(h):
    for i in range(N):
        for j in range(N):
            if area[i][j] <= h:
                chk[i][j] = True

def safe():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if chk[i][j] == True:
                continue
            queue = [[i,j]]
            chk[i][j] = True
            while queue:
                p,q = queue.pop()
                for k in range(4):
                    I = p+dx[k]
                    J = q+dy[k]
                    if 0 <= I < N and 0 <= J < N and not chk[I][J]:
                        chk[I][J] = True
                        queue.append([I,J])
                        
            cnt += 1
    return cnt

result = 1
rainH = set()
for i in range(N):
    for j in range(N):
        rainH.add(area[i][j])

while rainH:
    H = rainH.pop()
    rain(H)
    result = max(result,safe())
    chk = [[False]*N for _ in range(N)]

print(result)