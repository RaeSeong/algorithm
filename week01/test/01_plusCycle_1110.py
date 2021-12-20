import sys
N = int(sys.stdin.readline())

def calc(n,cnt):
    next = n%10*10 + (n//10 + n%10)%10
    result = cnt + 1
    if next == N:
        print(result)
    else:
        calc(next,result)

calc(N,0)