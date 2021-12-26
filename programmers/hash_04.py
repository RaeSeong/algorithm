def solution(genres, plays):
    answer = []
    hashTable = {}
    for i in range(len(genres)):
        if genres[i] in hashTable:
            hashTable[genres[i]][0] += plays[i]
            if hashTable[genres[i]][2][0] < plays[i]:
                hashTable[genres[i]][2][1] = hashTable[genres[i]][2][0]
                hashTable[genres[i]][1][1] = hashTable[genres[i]][1][0]
                hashTable[genres[i]][2][0] = plays[i]
                hashTable[genres[i]][1][0] = i
            elif hashTable[genres[i]][2][1] < plays[i]:
                hashTable[genres[i]][2][1] = plays[i]
                hashTable[genres[i]][1][1] = i
        else:
            hashTable[genres[i]] = [plays[i],[i,-1],[plays[i],0]]
    print(hashTable)
    order = sorted(hashTable.items(), reverse=True, key = lambda x:x[1][0])
    print(order)
    for i in order:
        for j in hashTable[i[0]][1]:
            if j != -1:
                answer.append(j)
    print('order',order)
    for i in order:
        print(hashTable[i[0]])
    print(answer)
    return answer

solution(["classic", "pop", "classic", "classic", "pop","rnb","rnb","rnb","balad","rock"],[500, 600, 150, 800, 2500,3000,7000,7000,1,999999])