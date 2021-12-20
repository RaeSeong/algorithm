import sys
N,M = map(int,sys.stdin.readline().split())
treeH = list(map(int,sys.stdin.readline().split()))
treeH.sort(reverse=True)
row = 0
high = treeH[0] - 1
while row <= high:
    mid = (row + high) // 2
    get = 0
    for i in treeH:
        if i <= mid:
            break
        get += i - mid
    if get >= M:
        row = mid + 1
    else:
        high = mid - 1
    # print(row,high)
print(high)
# treeH.sort(reverse=True)
# def new_func(M, treeH):
#     cutH = treeH[0]-1
#     while True:
#         getlog = 0 
#         cnt = 0   
#         for i in treeH:
#             cnt +=1
#             if cutH >= i:
#                 cnt -= 1
#                 break
#             else:
#                 cutTree = i - cutH
#                 getlog += cutTree

#         # print(cutH,getlog,cnt,cutH*3//2,cutH//2)
#         if getlog >= M and getlog < M + cnt:
#             break
#         if getlog > M:
#             cutH = (cutH+1)*3//2
#         elif getlog < M:
#             cutH = (cutH+1)//2
#     return cutH

# cutH = new_func(M, treeH)
    

# print(cutH)