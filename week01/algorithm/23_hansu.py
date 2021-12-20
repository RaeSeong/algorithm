a = input()
result = 0
for i in range(int(a)):
    if i < 99:
        result += 1
    else:
        A = list(map(int,str(i+1)))
        if A[0]-A[1] == A[1]-A[2]:
            result += 1
print(result)


