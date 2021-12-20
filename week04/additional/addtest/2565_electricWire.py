import sys
N = int(sys.stdin.readline())
wire = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
wire.sort()
cross = [[] for _ in range(wire[N-1][0]+1)]
for i in range(N):
    for j in range(i+1,N):
        if wire[i][1] > wire[j][1]:
            cross[wire[j][0]].append(wire[i][0])
            cross[wire[i][0]].append(wire[j][0])
remove = 0

crosslen = [len(i) for i in cross]
while True:
    if sum(crosslen) == 0:
        break
    l = crosslen.index(max(crosslen))
    # print(l,'????')
    for i in range(max(crosslen)):
        a = cross[l].pop()
        crosslen[a] -= 1
    crosslen[l] = 0
    remove += 1
    # print(cross[l])
    # print(crosslen)
    # print(cross)

print(remove)
# longest = 0
# for i in cross:
#     longest = max(len(i),longest)
#     print(len(i))
# print(longest)
# cross[longest] = []
# for i in cross:
#     for j in i:
#         if j == longest:
#             del j
'''
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6
'''