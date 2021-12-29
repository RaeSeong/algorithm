def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    for idx,val in enumerate(answers):
        if one[idx%5] == val:
            score[0] += 1
        if two[idx%8] == val:
            score[1] += 1
        if three[idx%10] == val:
            score[2] += 1
    highest = max(score)
    answer = []
    for idx,i in enumerate(score):
        if i == highest:
            answer.append(idx+1)
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))