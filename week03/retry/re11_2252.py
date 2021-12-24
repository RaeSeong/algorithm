import sys
sys.setrecursionlimit(10**9)
N,M = map(int,sys.stdin.readline().split())
compare = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
smaller = [[] for _ in range(N+1)]
chk = [False for _ in range(N+1)]

for i in compare:
    smaller[i[1]].append(i[0])

student = []
def row(a):
    while smaller[a]:
        b = smaller[a].pop()
        if not chk[b]:
            chk[b] = True
            row(b)

    student.append(a)

for i in range(N):
    if chk[i+1]:
        continue
    chk[i+1] = True
    row(i+1)
print(*student)