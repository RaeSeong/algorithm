from collections import deque
def solution(priorities, location):
    answer = 0
    order = {}
    for i in priorities:
        if i in order:
            order[i] += 1
        else:
            order[i] = 1
    priorities = deque(priorities)
    while priorities:
        printer = priorities.popleft()
        if printer == max(order):
            answer += 1
            order[max(order)] -= 1
            if order[max(order)] == 0:
                del order[max(order)]
            if location == 0:
                return answer
        else:
            priorities.append(printer)
        location = (location-1)%len(priorities)

print(solution([2,1,3,2],2))
print(solution([1, 1, 9, 1, 1, 1],0))