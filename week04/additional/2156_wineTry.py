import sys
n = int(sys.stdin.readline())
qty = [int(sys.stdin.readline()) for _ in range(n)]
total = [0]*n
total[0] = qty[0]
if n > 1:
    total[1] = qty[0]+qty[1]
for i in range(2,n):
    total[i] = max(total[i-3] + qty[i-1] + qty[i],total[i-2] + qty[i],total[i-1])

# print(total)
print(max(total))