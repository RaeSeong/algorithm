import sys
n = int(sys.stdin.readline())
people = []
for i in range(n):
    h,o = list(map(int,sys.stdin.readline().split()))
    people.append([h,o,abs(h-o)])
raillen = int(sys.stdin.readline())
people.sort()
print(people)