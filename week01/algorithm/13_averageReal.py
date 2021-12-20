a = int(input())

for i in range(a):
    A = list(map(int,input().split()))
    sum = 0
    for j in A:
        sum = sum + j
    avg = (sum - A[0])/A[0]
    higherNum = 0
    k = 1
    
    while k < len(A):
        if A[k] > avg:
            higherNum = higherNum + 1
        k = k+1

    result = round(100*higherNum/A[0],3)
    print(f'{result:.3f}%')