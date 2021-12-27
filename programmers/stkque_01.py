def solution(progresses, speeds):
    answer = []
    done = 1
    day = 0
    for i in range(len(progresses)):
        if progresses[i] + day*speeds[i] >= 100:
            done += 1
            if len(progresses) == i+1:
                answer.append(done)
        else:
            if i != 0:
                answer.append(done)
            print(day,((progresses[i]+day*speeds[i] - 100)//speeds[i]))
            day -= ((progresses[i]+day*speeds[i] - 100)//speeds[i])
            done = 1

    return answer

print(solution([93, 30, 55],[1,30,5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))