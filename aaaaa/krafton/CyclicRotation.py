from collections import deque

def solution(A, K):
    if A:
        for i in range(K):
            A = deque(A)
            A.appendleft(A.pop())
    return list(A)

print(solution([3, 8, 9, 7, 6], 3))