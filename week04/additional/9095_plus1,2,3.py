import sys
T = int(sys.stdin.readline())
n = [int(sys.stdin.readline()) for _ in range(T)]
N = max(n)
ott = [0]*(N+1)
ott[1],ott[2],ott[3] = 1,2,4
for i in range(1,N-2):
    ott[i+3] = ott[i+2] + ott[i+1] + ott[i]

for i in n:
    print(ott[i])
