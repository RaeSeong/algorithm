import sys

# n,r,c = map(int,sys.stdin.readline().split())

#결과를 배열로 나타내는 함수
# size = int(sys.stdin.readline())
# order = []
def Z(N,arr = []):
    if N > 1:
        Z(N-1,arr+[0])
        Z(N-1,arr+[1])
        Z(N-1,arr+[2])
        Z(N-1,arr+[3])
    if N == 1:
        quad = 0
        x = 0
        y = 0
        for i in range(len(arr)):
            quad += 4**(len(arr)-1-i)*arr[i]
            if arr[i] == 2 or arr[i] == 3:
                x += 2**(len(arr)-1-i)
            if arr[i] == 1 or arr[i] == 3:
                y += 2**(len(arr)-1-i)
        order.append([x,y,quad])
# Z(size+1,[])
# print(list(sorted(order)))

def cnt(n,r,c):
    result = 0
    r = r
    c = c
    for i in range(n):
        Vbin = 2**(n-1-i) # 반 값을 저장
        quad = 0 # 몇 사분면에 존재하는지
        if Vbin <= r:
            quad += 2
            r = r - Vbin
        if Vbin <= c:
            quad += 1
            c = c - Vbin
        result += 4**(n-1-i)*quad # 각 사분면에 접근할 때 초기값을 더함

    return result

print(cnt(n,r,c))