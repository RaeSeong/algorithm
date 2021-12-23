import sys
N,M = map(int,sys.stdin.readline().split())
scales = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
lighter = [[] for _ in range(N+1)]
heavier = [[] for _ in range(N+1)]
for i in scales:
    lighter[i[0]].append(i[1])
    heavier[i[1]].append(i[0])

def countlighter(start):
    cnt = 0
    chk = [False for _ in range(N+1)]
    stack = [start]
    while stack:
        a = stack.pop()
        for i in lighter[a]:
            if not chk[i]:
                chk[i] = True
                cnt += 1
                stack.append(i)
    return cnt

def countheavier(start):
    cnt = 0
    chk = [False for _ in range(N+1)]
    stack = [start]
    while stack:
        a = stack.pop()
        for i in heavier[a]:
            if not chk[i]:
                chk[i] = True
                cnt += 1
                stack.append(i)
    return cnt

result = 0
for i in range(1,N+1):
    if countheavier(i) > N//2:
        result += 1
    if countlighter(i) > N//2:
        result += 1

print(result)
