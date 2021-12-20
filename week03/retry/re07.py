import sys
from collections import deque as dq
R,C = map(int,sys.stdin.readline().split())
alpha = [list(map(ord,list(sys.stdin.readline().rstrip()))) for _ in range(R)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
queue = dq([0,0])








# import sys
# from collections import deque as dq
# R,C = map(int,sys.stdin.readline().split())
# alpha = [list(map(ord,list(sys.stdin.readline().rstrip()))) for _ in range(R)]
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# queue = dq([0,0])
# print(alpha)
# def dfs(a,b,chk=[]):
#     chk.append(alpha[a][b])
#     for i in range(4):
#         A = a+dx[i]
#         B = b+dy[i]
#         if 0 <= A < R and 0 <= B < C and alpha[A][B] not in chk:
#             dfs(A,B,chk)