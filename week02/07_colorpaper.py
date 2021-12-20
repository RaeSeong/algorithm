import sys
size = int(sys.stdin.readline())
Smatrix = []
for i in range(size):
    Smatrix.append(list(map(int,sys.stdin.readline().split())))
white = 0
blue = 0
def cutORcnt(matrix,n):
    global white, blue
    if n == 0:
        return
    if n == 1:
        if matrix[0][0] == 0:
            print(0)
            white +=1
        else:
            print(1)
            blue +=1

    half = int(n/2)
    print(n,half,matrix)
    if matrix[0:half-1] == matrix[half:n]:
        if matrix[0][0] == 0:
            white += 1
        else:
            blue +=1
    else:
        matrix1 = []
        for i in range(half):
            matrix1.append(matrix[i][0:half-1])
        matrix2 = []
        for i in range(half):
            matrix2.append(matrix[i][half:n-1])
        matrix3 = []
        for i in range(half):
            matrix3.append(matrix[half+i][0:half-1])
        matrix4 = []
        for i in range(half):
            matrix4.append(matrix[half+i][half:n-1])
        cutORcnt(matrix1,half)
        cutORcnt(matrix2,half)
        cutORcnt(matrix3,half)
        cutORcnt(matrix4,half)
    
    # except:
    #     if matrix[0][0] == 0:
    #         white.append(0)
    #     else:
    #         blue.append(1)

cutORcnt(Smatrix,size)
print(list(white),blue)