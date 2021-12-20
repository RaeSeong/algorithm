import sys
N = int(sys.stdin.readline())
n = 1000
num = list(map(int,sys.stdin.readline().split()))
primeN = set(i for i in range(2,n+1))
for i in range(2, int(n**0.5+1)):
    for j in range(2, int(n/i + 1)):
        try:
            primeN.remove(i*j)
        except:
            continue
count = 0

for i in num:
    if i in primeN:
        count += 1

print(count)