# 이상하게 해부렀네;
import sys
N = int(sys.stdin.readline())
arrN = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arrM = list(map(int,sys.stdin.readline().split()))

arrN.sort()

def find(num):
    left = 0
    right = len(arrN)
    idx = right//2
    while(True):
        if arrN[idx] == num:
            return 1
        if idx == left:
            return 0
        if arrN[idx] < num:
            left = idx
        else:
            right = idx
        idx = (left+right)//2

for i in arrM:
    print(find(i))