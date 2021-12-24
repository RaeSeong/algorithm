import sys
N,M = map(int,sys.stdin.readline().split())
compare = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
after = [[] for _ in range(N+1)]
inde = [0]*(N+1)
result = []

for i in compare:
    after[i[0]].append(i[1])
    inde[i[1]] += 1

queue = []
for i in range(1,N+1):
    if inde[i] == 0:
        queue.append(i)

while queue:
    turn = queue.pop()
    result.append(turn)
    while after[turn]:
        a = after[turn].pop()
        inde[a] -= 1
        if inde[a] == 0:
            queue.append(a)

print(*result)