import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
build = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
need = [[0]*N for _ in range(N+1)]
# basic = [True]*(N+1)
# result = [0]*(N+1)

# for i in build:
#     need[i[0]][i[1]] += i[2]
#     basic[i[0]] = False

# def cnt(part, ea):
#     if basic[part]:
#         result[part] += ea
#         return

#     for i in range(1,N):
#         if need[part][i] > 0:
#             cnt(i, need[part][i]*ea)

# cnt(N,1)

# for i in range(1,N+1):
#     if basic[i] and result[i] != 0:
#         print(i, result[i])