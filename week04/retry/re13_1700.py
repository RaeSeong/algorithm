import sys
N,K = map(int,sys.stdin.readline().split())
use = list(map(int,sys.stdin.readline().split()))
tap = [0]*N
pull = 0









# tap = [0]*N
# ptr = 0

# pull = 0
# for i in range(K):
#     ready = False
#     print(tap)
#     for j in range(ptr):
#         if tap[j] == use[i]:
#             ready = True
#             break
#     if not ready:
#         if ptr <= N-1:
#             tap[ptr] = use[i]
#             ptr += 1
#         else:
#             reuse = []
#             j = 0
#             more = 0
#             while j < K - i - 1 and j < N+more:
#                 for k in range(N):
#                     if tap[k] == use[i+1+j]:
#                         if use[i+1+j] in reuse:
#                             more += 1
#                             break
#                         reuse.append(k)
#                 j += 1
#             pull += 1
#             for j in range(N):
#                 if j not in reuse:
#                     tap[j] = use[i]
#                     break

# print(pull)
