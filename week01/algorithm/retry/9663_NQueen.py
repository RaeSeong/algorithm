import sys
sys.setrecursionlimit(10**8)
N = int(sys.stdin.readline())


def queen(loc, row, n):
    cnt = 0
    if row == n:
        return 1
    for i in range(N):
        loc[row] = i
        for j in range(row):
            if loc[j] == loc[row] or abs(loc[j] - loc[row]) == row - j:
                break
        else:
            cnt += queen(loc, row + 1, n)
    return cnt

def result(n):
    return queen([0]*n,0,n)

print(result(N))