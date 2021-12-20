import sys
N, R, C = map(int,sys.stdin.readline().split())

board = [[0]*(2**N) for _ in range(2**N)]

def Z(n,r,c,add):
    if n == 1:
        board[r][c] = add + 0
        board[r][c+1] = add + 1
        board[r+1][c] = add + 2
        board[r+1][c+1] = add + 3
        return
    
    Z(n-1,r,c,add)
    Z(n-1,r,c + 2**(n-1), add + 2**(2*n-2))
    Z(n-1,r + 2**(n-1),c, add + 2**(2*n-2)*2)
    Z(n-1,r + 2**(n-1),c + 2**(n-1), add + 2**(2*n-2)*3)

# Z(N,0,0,0)

# for i in board:
#     print(i)

def idx(n,r,c,result):
    if r == c == 0:
        return result
    half = 2**(n-1)
    if r < half:
        if c < half:
            return idx(n-1,r,c,result)
        else:
            result += half**2
            return idx(n-1,r,c-half,result)
    else:
        if c < half:
            result += (half**2)*2
            return idx(n-1,r-half,c,result)
        else:
            result += (half**2)*3
            return idx(n-1,r-half,c-half,result)

print(idx(N,R,C,0))