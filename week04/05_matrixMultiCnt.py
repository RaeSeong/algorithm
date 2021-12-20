import sys
N = int(sys.stdin.readline())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
val = [[float('inf')]*(N+1) for _ in range(N+1)]
for i in range(N+1):
    for j in range(N+1):
        if i == j:
            val[i][j] = 0
# for i in range(N):
#     for j in range(N):
#         if j - i == 1:
#             val[i][j] = matrix[i][0]*matrix[j][0]*matrix[j][1]

# for i in range(N):
#     for j in range(N):
#         if j - i == 2:
#             val[i][j] = min(val[i][j-1] + matrix[i][0]*matrix[j][0]*matrix[j][1],val[i+1][j] + matrix[i][0]*matrix[i][1]*matrix[j][1])

# for i in range(N):
#     for j in range(N):
#         if j - i == 3:
#             val[i][j] = [val[i][j-1] + matrix[i][0]*matrix[j][0]*matrix[j][1], val[i+1][j] + matrix[i][0]*matrix[i][1]*matrix[j][1], val[i][j-2] + val[i-2][j] + matrix[i][0]*matrix[j-1][0]*matrix[j][1]]
            
for i in range(N):
    for j in range(N):
        for k in range(j-i):
            # print(i,j,k,val[i][j],val[i][j-1-k]+val[i+1+k][j] + matrix[i][0]*matrix[j-k][0]*matrix[j][1])
            val[i][j] = min(val[i][j],val[i][j-1-k]+val[i+1+k][j] + matrix[i][0]*matrix[j-k][0]*matrix[j][1])


print(matrix)
for i in val:
    print(i)

# 1.1 = val[i][i+1] + matrix[i][0]*matrix[i+1][0]*matrix[i+1][1]
# ##########
# 2.1 = val[i][i+1] + matrix[i][0]*matrix[i+2][0]*matrix[i+2][1]
# 2.2 = val[i+1][i+2] + matrix[i][0]*matrix[i][1]*matrix[i+2][1]
# ##########
# 3.1 = val[i][i+2] + matrix[i][0]*matrix[i+3][0]*matrix[i+3][1]
# 3.2 = val[i+1][i+3] + matrix[i][0]*matrix[i+1][0]*matrix[i+3][1]
# 3.3 = val[i][i+1] + val[i-2][i+3] + matrix[i][0]*matrix[i+2][0]*matrix[i+3][1]
# # calc = []
# for i in range(N-1):
#     a,b,c = matrix[i][0],matrix[i][1],matrix[i+1][1]
#     calc.append([a,b,c])