import sys
sys.setrecursionlimit(10**8)
N = int(sys.stdin.readline())
area = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
rain = set()
for i in range(N):
    rain |= set(area[i])

def safe_cnt(height):
    safe_zone = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if area[i][j] > height:
                safe_zone[i][j] = True
    
    cnt = 0
    for i in range(N):
        for j in range(N):
            if safe_zone[i][j] == True:
                safe_zone[i][j] = False
                dfs(i,j,safe_zone)
                cnt += 1
    
    return cnt

def dfs(a,b,safe_zone):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]            
    for i in range(4):
        A = a + dx[i]
        B = b + dy[i]
        if 0 <= A < N and 0 <= B < N and safe_zone[A][B] == True:
            safe_zone[A][B] = False
            dfs(A,B,safe_zone)


safe_max = 1
for i in rain:
    new = safe_cnt(i)
    if new > safe_max:
        safe_max = new

print(safe_max)