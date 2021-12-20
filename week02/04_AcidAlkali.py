import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()

left = 0
right = len(arr)-1
if arr[left] > 0 and arr[right] > 0:
    arr[left]+arr[right]



