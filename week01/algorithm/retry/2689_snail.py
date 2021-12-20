import sys
A,B,V = map(int,sys.stdin.readline().split())

lastday = V - A
if lastday == 0:
    print(1)
else:
    up = A-B
    if lastday%up == 0:
        print(lastday // up + 1)
    else:
        print(lastday // up + 2)
