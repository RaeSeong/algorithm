n = int(input())

for i in range(n):
    k = ''
    for j in range(i+1):
        k = k + '*'
    print(k)