import sys
N = int(sys.stdin.readline())
queue = []
ptr = 0

for i in range(N):
    if i%2 == 1:
        queue.append(i+1)
        
if N%2 == 1:
    queue.append(queue[ptr])
    ptr += 1

discard = 1
while ptr < len(queue):
    if discard == 0:
        queue.append(queue[ptr])
        discard += 1
    else:
        discard -= 1
    ptr += 1

if N == 1:
    print(1)
else:
    print(queue[ptr-1])