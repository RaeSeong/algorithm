import sys
import itertools
cnt = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))


nPr = list(itertools.permutations(arr,cnt))
result = 0
for j in range(len(nPr)):
    sum = 0
    for i in range(cnt-1):
        sum += abs(nPr[j][i]-nPr[j][i+1])
        if i == cnt-2:
            if sum > result:
                result = sum

print(result)

