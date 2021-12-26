def solution(phone_book):
    hashTable = {}
    
    for i in phone_book:
        hashTable[hash(i)] = 1
    
    for i in phone_book:
        jd = ''
        for j in i:
            jd += j
            if hash(jd) in hashTable and jd != i:
                return False
    return True

solution(["119", "97674223", "1195524421"])