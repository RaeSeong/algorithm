import sys
N = int(sys.stdin.readline())
An = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Am = list(map(int,sys.stdin.readline().split()))

An.sort()

for i in Am:
    left = 0
    right = len(An) - 1
    a = 0
    while left <= right:
        mid = (left + right) // 2
        if An[mid] > i:
            right = mid - 1
        elif An[mid] < i:
            left = mid + 1
        else:
            a = 1
            break
    print(a)



# for i in range(len(Am)):
#     left = 0
#     right = len(An)-1
#     while True:    
#         if left > right:
#             print(0)
#             break
#         if An[(left+right)//2] > Am[i]:
#             right = (left+right)//2 - 1
#         elif An[(left+right)//2] < Am[i]:
#             left = (left+right)//2 + 1
#         else:
#             print(1)
#             break
