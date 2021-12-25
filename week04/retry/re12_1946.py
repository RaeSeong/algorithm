import sys
T = int(sys.stdin.readline())
answer = []
for i in range(T):
    cnt = int(sys.stdin.readline())
    apply = [list(map(int,sys.stdin.readline().split())) for _ in range(cnt)]
    apply.sort(key=lambda x: (x[0],x[1]))
    employ = 0
    cutline = apply[0][1]
    for i in apply:
        if i[1] <= cutline:
            cutline = i[1]
            employ += 1

    answer.append(employ)

for i in answer:
    print(i)