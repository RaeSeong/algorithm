n = int(input())
A = list(map(int,input().split()))
result = len(A)
prime = ''
for i in A:
    for j in range(i-2):
        if i%(j+2) == 0:
            prime = 'X'
    if prime == 'X' or i == 1:
        result = result - 1
        prime = ''

print(result)