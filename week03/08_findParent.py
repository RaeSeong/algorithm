import sys
from collections import defaultdict as dd
sys.setrecursionlimit(10**9)
N = int(sys.stdin.readline())
tree = dd(list)
for _ in range(N-1):
    x,y = map(int,sys.stdin.readline().split())
    tree[x].append(y)
    tree[y].append(x)

parent = [0 for _ in range(N+1)]

# def find(v,chk=[]):
#     for i in tree[v]:
#         if i not in chk:
#             chk.append(i)
#             parent[i] = v
#             find(i,chk)

def find(v):
    for i in tree[v]:
        if parent[i] == 0:
            parent[i] = v
            find(i) 

# find(1,[1])
# for i in range(2,N+1):
#     print(parent[i])

find(1)
for i in range(2,N+1):
    print(parent[i])