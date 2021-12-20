import sys
N,K = map(int,sys.stdin.readline().split())
useorder = list(map(int,sys.stdin.readline().split()))
tap = [0]*N
nextuse = [0]*N
index = 0
cnt = 0
for i in range(K):
    a = 1
    for j in tap:
        if useorder[i] == j:
            a = 0
            break
    if a == 0:
        continue
    if index <= len(tap)-1:
        tap[index] = useorder[i]
        index += 1
    else:
        for j in range(N):
            for k in range(i,K):
                if tap[j] == useorder[k]:
                    nextuse[j] = k
                    break
                nextuse[j] = K+1
        tap[nextuse.index(max(nextuse))] = useorder[i]
        cnt += 1
    nextuse = [0]*N
    
print(cnt)














# tap = [0]*N
# fix = []
# cnt = 0
# for i in range(K-N):
#     for j in range(N):
#         if useorder[i] == useorder[i+j+1]:
#             fix.append(useorder[i])
#     for j in range(N):
#         if tap[j] not in fix:
#             tap[j] = i
#             cnt += 1
            

# print(cnt)