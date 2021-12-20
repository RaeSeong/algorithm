n = int(input())
for c in range(n):
    a = list(input().split(' ',2))
    result = ''
    for i in list(a[1]):
        for j in range(int(a[0])):
            result = result + str(i)
    print(result)