n,x = map(int,input().split())

A = list(map(int,input().split()))

result = ''
for i in A:
    if x > i :
        result = result + ' ' + str(i)
print(result.lstrip())