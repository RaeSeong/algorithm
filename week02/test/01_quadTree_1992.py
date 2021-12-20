import sys
N = int(sys.stdin.readline())
matrix = list(list(map(int,sys.stdin.readline().rstrip())) for _ in range(N))
result = []

def vediozip(n,ud,lr):
    result.append('(')
    matrix0 = 0
    matrix1 = 0
    matrix2 = 0
    matrix3 = 0
    print(n,ud,lr)
    if n == 0:
        result.append(matrix[ud][lr])
        result.append(matrix[ud][lr+1])
        result.append(matrix[ud+1][lr])
        result.append(matrix[ud+1][lr+1])
    else:
        for i in range(2**(n-1)):
            for j in range(2**(n-1)):
                matrix0 += matrix[i+ud][j+lr]
                matrix1 += matrix[i+ud][2**(n-1)+j+lr] 
                matrix2 += matrix[2**(n-1)+i+ud][j+lr]
                matrix3 += matrix[2**(n-1)+i+ud][2**(n-1)+j+lr]
        if matrix0 == 0:
            result.append('0')
        elif matrix == 4**(n-1):
            result.append('1')
        else:
            vediozip(n-1,ud,lr)

        if matrix0 == 0:
            result.append('0')
        elif matrix == 4**(n-1):
            result.append('1')
        else:
            vediozip(n-1,ud,lr+2**(n-1))

        if matrix0 == 0:
            result.append('0')
        elif matrix == 4**(n-1):
            result.append('1')
        else:
            vediozip(n-1,ud+2**(n-1),lr)

        if matrix0 == 0:
            result.append('0')
        elif matrix == 4**(n-1):
            result.append('1')
        else:
            vediozip(n-1,ud+2**(n-1),lr+2**(n-1))
    result.append(')')

vediozip(3,0,0)
print(result)