def solution(A):
    choose = [False]*1000000
    for i in A:
        if i > 0:
            choose[i-1] = True
    
    for idx,i in enumerate(choose):
        if i:
            return idx+1
    return 1