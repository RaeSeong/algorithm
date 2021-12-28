def solution(N):
    answer = 0
    tmp = 0
    on = False
    for i in range(1,64):
        if N < 2**i:
            return max(answer,tmp)
        if N%(2**i) == 0:
            if on == True:
                tmp += 1
        else:
            if on == False:
                on = True
            else:
                answer = max(answer,tmp)
                tmp = 0
            N -= 2**(i-1)

print(solution(1041))