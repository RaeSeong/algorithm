#시간초과
def prime(num):
    A = []
    for i in range(2,4999):
        prime = ''
        for j in range(i-2):
            if i%(i-j-1) == 0:
                prime = 'X'
        if prime == '':
            A.append(i)
    if num in A:
        return True
    else:
        return False

for cnt in range(int(input())):
    a = int(input())
    if int(a/2)%2 == 0 and a != 4:
        first = int(a/2) - 1
    else:
        first = int(a/2)
    result = 0
    while True:
        if prime(first) == True:
            if prime(a-first) == True:
                result = first
                break
        first -= 2

    print(result,a-result)

#시간초과
# A = []
# for i in range(2,4999):
#     prime = ''
#     for j in range(i-2):
#         if i%(i-j-1) == 0:
#             prime = 'X'
#     if prime == '':
#         A.append(i)

# for cnt in range(int(input())):
#     a = int(input())
#     first = int(a/2)
#     if first != 2 and first%2 == 0:
#         first = first - 1
#     while True:
#         if first in A:
#             if a - first in A:
#                 result = first
#                 break
#         first -= 2

#     print(first,a-first)

#시간초과로 실패
# for cnt in range(int(input())):
#     a = int(input())
#     # for i in range(a):
#     first = int(a/2)
#     prime1 = 'X'
#     prime2 = 'X'
#     while True:
#         prime1 = ''
#         for j in range(first-2):
#             if first%(first-1-j) == 0:
#                 prime1 = 'X'
#         if prime1 == '':
#             other = a - first
#             prime2 = ''
#             for k in range(other-2):
#                 if other%(other-1-k) == 0:
#                     prime2 = 'X'
#             if prime2 == '':        
#                 result = first
#                 break
#         first = first - 1

#     print(result,other)