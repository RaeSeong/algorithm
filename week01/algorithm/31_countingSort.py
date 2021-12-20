import sys
cnt = int(sys.stdin.readline())
numlist = [] #입력받을 배열
numvalue = [0]*10000 #분포표

# 입력 데이터 받기 + 배열에 추가 + 분포표 값 업데이트
for i in range(cnt):
    value = int(sys.stdin.readline())
    numlist.append(value)
    numvalue[value-1] += 1

#누적분포표 만들기
for j in range(1,10000):
    numvalue[j] += numvalue[j-1]

#작업용 배열 생성
leng = len(numlist)
sortlist = [0]*leng
for k in range(leng):
    org = numlist[leng-1-k] #정렬 전 배열의 맨 뒤부터 값 가져오기
    sortlist[numvalue[org-1]-1] = org #가져온 값을 작업용 배열에 위치시키기
    numvalue[org-1] -= 1 #같은 위치로 들어가지 않도록 작업

#정렬된 배열 출력
for m in range(leng):
    print(sortlist[m])