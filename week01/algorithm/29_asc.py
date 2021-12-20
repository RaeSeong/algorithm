import sys
cnt = int(sys.stdin.readline()) #목록 갯수
numL = [] 

#입력받은 목록 배열에 추가
for i in range(cnt):
    numL.append(int(sys.stdin.readline()))

#버블정렬
for k in range(cnt):
    for j in range(cnt-k): 
        if numL[cnt-1-j] < numL[cnt-1-j-1]:
            numL[cnt-1-j], numL[cnt-1-j-1] = numL[cnt-1-j-1], numL[cnt-1-j]

for m in numL:
    print(m)