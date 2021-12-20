import sys
calc = sys.stdin.readline().rstrip()
cnt = 1
result = 0
temp = []
minus = False
for i in calc:
    if i == '-' or i == '+':
        L = len(temp)
        for j in range(L):
            a,b = temp.pop()
            if minus:
                result -= a*(10**(L-b))
            else:
                result += a*(10**(L-b))
        if i == '-':
            minus = True
        cnt = 1
    else:
        temp.append([int(i),int(cnt)])
        cnt += 1

L = len(temp)
for j in range(L):
    a,b = temp.pop()
    if minus:
        result -= a*(10**(L-b))
    else:
        result += a*(10**(L-b))

print(result)
# plus = []
# minus = []
# for i in calc:
#     if i == '-':
#         break
#     else:
#         plus.append(i)

# for i in range(len(plus)+1,len(calc)):
#     minus.append(calc[i])

# print(*plus)
# print(*minus)