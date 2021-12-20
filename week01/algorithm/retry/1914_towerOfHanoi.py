import sys

N = int(sys.stdin.readline())

def TOH(n,start,end):
    if n < 1:
        return
    TOH(n-1,start,6 - start - end)
    print(start,end)
    TOH(n-1,6 - start - end, end)


print(2**N - 1)
if N <= 20:
    TOH(N,1,3)