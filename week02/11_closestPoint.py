import sys
N = int(sys.stdin.readline())
coordinate = []
for i in range(N):
    coordinate.append(sys.stdin.readline().rstrip())

each = set(coordinate)

if len(each) < N:
    print(0)
else:
    sorted(each)