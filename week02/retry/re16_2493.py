import sys
N = int(sys.stdin.readline())
towers = list(map(int,sys.stdin.readline().split()))
signal = []
result = []

for i in range(N):
    while True:
        if not signal:
            signal.append([towers[i],i+1])
            result.append(0)
            break
        else:
            height, num = signal.pop()
            if height > towers[i]:
                signal.append([height,num])
                signal.append([towers[i],i+1])
                result.append(num)
                break
            else:
                continue
        

print(*result)