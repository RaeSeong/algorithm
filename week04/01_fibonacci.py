import sys
n = int(sys.stdin.readline())
fibo = [0]*91
fibo[1] = 1
for i in range(n-1):
    fibo[i+2] = fibo[i+1]+fibo[i]

print(fibo[n])