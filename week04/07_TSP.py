import sys
N = int(sys.stdin.readline())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
# city = [[0]*(N+1) for _ in range(N)]
city = [[sum(max(matrix[i]) for i in range(N))]*(N+1) for _ in range(N)]
chk = [[False]*N for _ in range(N+1)]
for i in city:
    i[0] = 0
    print(i)


for k in range(1,N+1):
    for j in range(N):
        for i in range(N):
            print(i,j,k)
            for m in city:
                print(m)
            print('aaaaaaaaaaaaa')
            if matrix[i][j] == 0 or chk[i][j]:
                continue
            city[j][k] = min(city[j][k],city[i][k-1]+matrix[i][j])
            if city[j][k] == city[i][k-1]+matrix[i][j]:
                chk[i][j] = True
                chk[i-1][j] = False
print('------------------')
for i in city:
    print(i)