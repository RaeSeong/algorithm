import sys
N = int(sys.stdin.readline())
tile = [0]*(N+4)
tile[1] = 1
tile[2] = 2
tile[3] = 3
for i in range(1,N-2):
    tile[i+3] = (2*tile[i+1]+tile[i])%15746



print(tile[N])