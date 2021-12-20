import sys
N = int(sys.stdin.readline())
val = [N//3+1]*(N+1)
val[1] = 0
for i in range(2,N+1):
    if i%3 == 0:
        if i%2 == 0:
            val[i] = min(val[i//3],val[i//2],val[i-1]) + 1
        else:
            val[i] = min(val[i//3],val[i-1]) + 1
    elif i%2 == 0:
        val[i] = min(val[i//2],val[i-1]) + 1
    else:
        val[i] = val[i-1] + 1

print(val[N])