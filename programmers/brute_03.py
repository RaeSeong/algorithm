def solution(brown, yellow):
    other = brown//2 + 2
    for i in range(1,other):
        print(other,i)
        if i*(other-i) == yellow+brown:
            return [other-i, i]
        

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))