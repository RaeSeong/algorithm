import sys
a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())
chk = [[0]*(len(b)+1) for _ in range(len(a)+1)]
for i in range(1,len(b)+1):
    for j in range(1,len(a)+1):
        if b[i-1] == a[j-1]:
            chk[j][i] = chk[j-1][i-1] + 1
        else:
            chk[j][i] = max(chk[j-1][i],chk[j][i-1])


print(chk[-1][-1])


# if len(a)<len(b):
#     A,B = b,a
# result = []
# common = []
# while B:
#     d = B.pop()
#     c = A.pop()
#     if d == c:
#         common.append(d)
#         continue
