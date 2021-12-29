def solution(A):
    total = sum(A)
    front = 0
    answer = 0
    for i in A:
        front += i
        if front >= total//2:
            answer = min(abs(total-2*front),abs(total-2*(front-i)))
            return answer

print(solution([3,1,2,4,3,9,9,9,9]))