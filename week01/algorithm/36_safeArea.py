import sys
size = int(sys.stdin.readline())
area = []
flood = []
for i in range(size):
    area.append(list(map(int,sys.stdin.readline().split())))
    flood.append([False]*len(area[i]))

maxH = max(map(max,area))

def search(matrix,line,row):
    if chk[line][row] == True:
        return
    Mlen = len(matrix)-1    
    chk[line][row] = True
    top = line-1
    bottom = line+1
    left = row-1
    right = row+1
    if top < 0:
        pass
    else:
        if matrix[top][row] == False:
            search(matrix,top,row)
    if bottom > Mlen:
        pass
    else:
        if matrix[bottom][row] == False:
            search(matrix,bottom,row)
    if left < 0:
        pass
    else:
        if matrix[line][left] == False:
            search(matrix,line,left)
    if right > Mlen:
        pass
    else:
        if matrix[line][right] == False:
            search(matrix,line,right)
    return 1

safe = 1

for j in range(1,maxH):
    for k in range(len(area)):
        for l in range(len(area[k])):
            if area[k][l] <= j:
                flood[k][l] = True
    chk = flood
    
    for k in range(len(area)):
        island = 0
        for l in range(len(area[k])):
            if flood[k][l] == False:
                island += search(flood,k,l)
                print(island,search(flood,k,l))
                if island > safe:
                    safe = island

    # print(list(flood))

print(safe)

