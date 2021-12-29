def solution(A):
    if len(A) == 1:
        if A[0] == 1:
            return 1
        return 0
    A.sort()
    if A[0] == 1 and A[1] - A[0] == 1 and A[-1]-A[0] == len(A)-1:
        return 1
    return 0

def solution(A):
    if len(A) == 1:
        if A[0] == 1:
            return 1
        return 0
    A.sort()
    if A[0] != 1:
        return 0
    for i in range(1,len(A)):
        if A[i]-A[i-1] != 1:
            return 0
    return 1