import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    rank = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    rank.sort()
    cut = rank[0][1]
    cnt = 1
    for i in range(1,N):
        if rank[i][1] < cut:
            cnt += 1
            cut = rank[i][1]
            

    print(cnt)