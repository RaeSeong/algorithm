import sys
N = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(N)]

n = 10000
primeN = set(i for i in range(2,n+1))
for i in range(2, int(n**0.5+1)):
    for j in range(2, int(n/i + 1)):
        try:
            primeN.remove(i*j)
        except:
            continue
# print(primeN)
for i in a:
    half = int(i/2)
    ok = False
    while(half > 1):
        if half in primeN:
            if i - half in primeN:
                ok = True
        if ok == True:
            break
        half -= 1
    print(half, i - half)
