a = list(input().split())
reverse1 = ''
for i in range(len(a[0])):
    reverse1 = reverse1 + list(a[0])[len(a[0])-1-i]
reverse2 = ''
for i in range(len(a[1])):
    reverse2 = reverse2 + list(a[1])[len(a[1])-1-i]

if reverse1 > reverse2:
    print(reverse1)
else:
    print(reverse2)