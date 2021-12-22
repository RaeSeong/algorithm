import sys
N = int(sys.stdin.readline())
ho = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
rail = int(sys.stdin.readline())

left = set()
for i in ho:
    left.add(ho[0])
    left.add(ho[1]-rail)
# possible = []

# left = set()
# right = set()
# for i in ho:
#     if(abs(i[1]-i[0])) <= rail:
#         left.add(i[0])
#         right.add(i[1])
#         possible.append(i)

# result = 0
# for i in left:
#     tmp = 0
#     railend = i + rail
#     for j in possible:
#         if i <= j[0] <= railend and i <= j[1] <= railend:
#             tmp += 1
#     if tmp > result:
#         result = tmp

# for i in right:
#     tmp = 0
#     railstart = i - rail
#     for j in possible:
#         if railstart <= j[0] <= i and railstart <= j[1] <= i:
#             tmp += 1
#     if tmp > result:
#         result = tmp

# print(result)