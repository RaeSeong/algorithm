import sys
N,K = map(int,sys.stdin.readline().split())
queue = []
ptr = 0
result = []

for i in range(1,N+1):
    queue.append(i)

while ptr < len(queue):
    ptr += 1
    if ptr%K != 0:
        queue.append(queue[ptr-1])
    else:
        result.append(queue[ptr-1])

print('<' + ', '.join(map(str,result)) + '>')