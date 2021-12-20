import sys
N = int(sys.stdin.readline())
circles = []
for i in range(N):
    x, y = map(int,sys.stdin.readline().split())
    circles.append([x-y,x+y])
circles.sort(reverse=True)
seper = []
a = circles.pop()
b = circles.pop()
a[0] == b[0]
a[1],b[1]

print(circles)
