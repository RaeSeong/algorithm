import sys
arr = list(sys.stdin.readline().strip().split('-'))

result = sum(list(map(int,arr[0].split('+')))) * 2
for i in arr:
    result -= sum(list(map(int,i.split('+'))))

print(result)