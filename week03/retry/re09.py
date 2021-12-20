import sys
from collections import deque as dq
N,M = map(int,sys.stdin.readline().split())
sea = [list(map(int,sys.stdin.readline().split())) for _ in range(N)] #초기 바다
meltsea = list(map(list,sea))   #녹은 후 데이터를 임시 저장하는 곳
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def melt(): #녹이는 함수
    global allmelt  #다 녹았는지 확인하는 변수
    for i in range(1,N-1):
        for j in range(1,M-1):  #테두리 바다를 제외한 나머지 칸에 대해 반복
            if sea[i][j] == 0:  #물이면 패스
                continue
            for k in range(4):  #얼음이면 상하좌우 확인
                I = i+dx[k]
                J = j+dy[k]
                if meltsea[i][j] > 0 and sea[I][J] == 0: #더 녹일 얼음이 남아있고 and 인접한 곳이 물이면
                    meltsea[i][j] -= 1  #인접한 물이 있을 때마다 하나씩 감소
                    allmelt = False #한 번이라도 녹였으면 아직 다 녹은 게 아님

chk = [[False]*M for _ in range(N)] #확인한 곳인지 저장할 공간
def seperate():
    part = 0    #덩어리 수 초기화
    for i in range(1,N-1):
        for j in range(1,M-1):  #테두리 바다를 제외한 나머지 칸에 대해 반복
            if meltsea[i][j] == 0 or chk[i][j]: #물이거나 체크했으면 패스
                continue
            if part == 1:   #덩어리가 이미 있으면 새로운 덩어리를 체크하려는 순간 이미 2개 이상이므로 분리됐다고 판단
                return True
            bfs = dq([[i,j]])   #덩어리 체크 시작 지점
            while bfs:  #시작지점으로부터 너비우선탐색 진행
                p,q = bfs.popleft() 
                chk[p][q] = True    #체크 여부 변경
                for k in range(4):  #상하좌우
                    I = p+dx[k]
                    J = q+dy[k]
                    if meltsea[I][J] > 0 and not chk[I][J]: #해당 지점이 얼음이고 and 체크하지 않았으면
                        chk[I][J] = True
                        bfs.append([I,J])   #탐색 지점 추가
            part = 1 #첫 번째 덩어리 탐색이 완료되면 값 부여
    return False #반복문이 완료될 때까지 두 번째 탐색이 시작되지 않아서 True를 return하지 않으면 덩어리는 분리되지 않았기 때문에 False반환
year = 1    #최초 덩어리는 하나짜리로 명시되었기 때문에 일단 판별 시작
ok = False  #분리됐는지 여부 False로 초기화
allmelt = True  #모두 녹았는지 여부 True로 초기화(melt()함수에서 하나라도 녹으면 False로 변환하게 됨)
while True: #녹이고-판단하고-초기화 반복
    melt()  #녹이고
    # for i in meltsea:
    #     print(i)
    # print('-------------------')
    if allmelt == True: #melt()함수에서 단 한 번도 녹이지 못 했으면
        print(0)    #모두 물이 된 상태로 판단, 0 출력
        break
    ok = seperate() #나뉘었는지 판단
    if ok:
        print(year) #나뉘었으면 이번 년도 출력
        break
    chk = [[False]*M for _ in range(N)] #덩어리 탐색 공간 초기화
    sea = list(map(list,meltsea))   #녹은 바다를 기본 바다로 대입
    year += 1   #다음 년도로 넘어감
    allmelt = True  #다 녹였는지 판단하는 값 초기화

# for i in meltsea:
#     print(i)
    