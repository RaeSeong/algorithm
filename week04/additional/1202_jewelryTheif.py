import sys
N,K = map(int,sys.stdin.readline().split())
gem = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
bag = [int(sys.stdin.readline()) for _ in range(K)]
gem.sort(key=lambda x:(x[1],x[0]),reverse=True)
bag.sort()
packidx = []
pack = [0]*K
for i in range(K):
    for j in range(N):
        if gem[j][0] <= bag[i] and j not in packidx:
            pack[i] = gem[j][1]
            packidx.append(j)
            break

print(sum(pack))











# idx = -1
# for i in range(K):
#     for j in range(len(gem)):
#         if gem[j][0] <= bag[i]:
#             if pack[i] < gem[j][1]:
#                 pack[i] = gem[j][1]
#                 idx = j
#     gem.pop(idx)

# print(sum(pack))

