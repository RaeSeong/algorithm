import sys
import itertools

#도시 순회 비용 계산 함수
def costCal(arr):
    cost = 0
    for i in range(len(arr)):
        if i == 0: #첫 번째 행
            if cityMt[0][arr[i]-1] == 0: #이동 비용이 0인 곳은 리턴
                return
            cost += cityMt[0][arr[i]-1] #
        else:
            if cityMt[arr[i-1]-1][arr[i]-1] == 0: #이동 비용이 0인 곳은 리턴
                return
            cost += cityMt[arr[i-1]-1][arr[i]-1]
    cost += cityMt[arr[len(arr)-1]-1][0]
    return cost

#입력 받기
cnt = int(sys.stdin.readline())
cityMt = []
seq = []
for i in range(cnt):
    cityMt.append(list(map(int,sys.stdin.readline().split())))
#1을 제외한 방문도시 목록
for j in range(2,cnt+1):
    seq.append(j)
#방문도시 순서 순열 값
seqP = list(itertools.permutations(seq,cnt-1))

minCost = 9999999999


for k in range(len(seqP)): #순열갯수만큼 반복
    cost = costCal(seqP[k])
    if cost == None:
        continue
    if cost < minCost:
        minCost = cost

print(minCost)

