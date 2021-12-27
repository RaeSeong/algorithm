def solution(bridge_length, weight, truck_weights):
    answer = 0
    cross = []
    done = 0
    now_weight = 0
    for i in truck_weights:
        while now_weight + i > weight:
            answer = cross[done][0] - 1
            now_weight -= cross[done][1]
            done += 1
        answer += 1
        cross.append([answer+bridge_length,i])
        now_weight += i

    answer += bridge_length
    return answer

print(solution(1,1,[1]))
print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,80,10,10,10,10,10,10]))
print(solution(10,10,[9,8,7,6,5,4,3,2,1,9]))
print(solution(10,10,[1,2,3,4,5,6,7,8,9,10]))