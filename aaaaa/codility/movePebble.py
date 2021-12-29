def solution(A):
    end = len(A)
    dp = [float('-inf')]*end
    dp[0] = 0
    for i in range(1,6):
        if end < i+1:
            return dp[end-1]
        for j in range(1,i+1):
            dp[i] = max(dp[i],dp[i-j]+A[i-j])

    for i in range(6,end):
        tmp = [0,float('-inf')]
        for j in range(6):
            if tmp[1] < A[i-j]:
                tmp = [j,A[i-j]]
        dp[i] = A[i-j]
    return dp[end-1] + A[end-1]

print(solution([-1,-2,0,-9,-1,-2,-5,-7,-10,-1,-1,-1,-1]))
solution([1,-2,0,9,-1,2,-5,-7,10])