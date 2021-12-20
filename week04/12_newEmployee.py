import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    rank = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    rank.sort()
    # possible = [True]*N
    # cnt = 0
    # for i in range(N):
    #     if rank[0][1] >= rank[i][1]:
    #         for j in range(N):
    #             if rank[i][0] > rank[j][0] and rank[i][1] > rank[j][1]:
    #                 possible[i] = False
    #                 break
    #         if possible[i]:
    #             cnt += 1

    possible = []
    for i in range(N):
        if rank[0][1] >= rank[i][1]:
            possible.append(rank[i])
    possible.sort(key = lambda x:x[1])

    possible2 = []
    for i in range(len(possible)):
        if possible[0][0] >= possible[i][0]:
            possible2.append(possible[i])

    cnt = len(possible2)
    for i in range(cnt):
        for j in range(cnt):
            if possible2[i][0] > possible2[j][0] and possible2[i][1] > possible2[j][1]:
                cnt -= 1
                break
    
    print(cnt)


    # rank.sort(reverse=True)
    # cnt = 2
    # a,b = rank.pop()
    # rank.sort(key = lambda x:x[1],reverse=True)
    # c,d = rank.pop()
    # if a == b:
    #     cnt -= 1
    # for i in range(N-2):
    #     if rank[i][0] < c and rank[i][1] < b:
    #         cnt += 1
    
    # print(cnt)