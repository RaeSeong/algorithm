def solution(X,A):
    leaves = [False]*X
    toX = 0
    answer = -1
    for i in A:
        if not leaves[i-1]:
            leaves[i-1] = True
            toX += 1
        answer += 1
        if toX == X:
            return answer
    return -1
print(solution(5,[1,3,1,4,2,3,5,4]))