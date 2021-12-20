import sys
# a = int(sys.stdin.readline())
# result = 1
# for i in range(1,a+1):
#     result *= i

# print(result)

def facto(num):
    if num == 1:
        return 1
    if num > 0:
        return num*facto(num-1)
    
print(facto(int(sys.stdin.readline())))
    