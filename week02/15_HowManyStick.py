import sys
N = int(sys.stdin.readline())
sticks = []
for i in range(N):
    sticks.append(int(sys.stdin.readline()))

visible = [0]

for j in range(len(sticks)):
    if visible[len(visible)-1] < sticks[len(sticks)-1-j]:
        visible.append(sticks[len(sticks)-1-j])

print(len(visible)-1)