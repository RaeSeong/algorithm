def solution(N,A):
    answer = [0]*N
    largest = 0
    for i in A:
        if i == N+1:
            answer = [largest]*N
        else:
            answer[i-1] += 1
            largest = max(largest,answer[i-1])
    return answer