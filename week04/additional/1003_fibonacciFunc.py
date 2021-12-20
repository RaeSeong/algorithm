from os import rename
import sys
T = int(sys.stdin.readline())
N = [int(sys.stdin.readline()) for _ in range(T)]
for n in N:
    fibo = [0]*(n+1)

    if n == 0:
        print(1,0)
    elif n == 1:
        print(0,1)
    else:
        fibo[1] = 1
        for i in range(2,n+1):
            fibo[i] = fibo[i-1] + fibo[i-2]

        print(fibo[n-1],fibo[n])