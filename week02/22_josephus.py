import sys
N,K = map(int,sys.stdin.readline().split())
arrN = []
for j in range(N):
    arrN.append(j+1)
msg = '<'
start = 0
i = 1
while True:
    index = start + K*i
    if index > len(arrN):
        start = index - len(arrN)
        index = start
        i = 1
    print(index, arrN)
    imsi = str(arrN.pop(index-1))
    print(imsi)
    msg += imsi
    start -= 1
    i += 1
    if len(arrN) == 0:
        msg += '>'
        break
    else:
        msg += ', '

print(msg)
