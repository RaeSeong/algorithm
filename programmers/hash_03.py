def solution(clothes):
    hashTable = {}
    hashList = []
    for i in clothes:
        if i[1] in hashTable:
            hashTable[i[1]] += 1
        else:
            hashTable[i[1]] = 1
            hashList.append(i[1])
    answer = 1
    for i in hashList:
        answer *= hashTable[i]+1
    answer -= 1
    return answer
print('abc')
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))