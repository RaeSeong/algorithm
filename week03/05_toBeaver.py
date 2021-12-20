import sys
from collections import deque as dq
R,C = map(int,sys.stdin.readline().split())
twmap = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

water = dq([])
route = dq([])
for i in range(R):
    for j in range(C):
        if twmap[i][j] == '*':
            water.append([i,j])
            twmap[i][j] = 0
        elif twmap[i][j] == 'S':
            route.append([i,j])
            twmap[i][j] = 0

def flood():
    while water:
        x,y = water.popleft()
        for i in range(4):
            X = x+dx[i]
            Y = y+dy[i]
            if 0 <= X < R and 0 <= Y < C and twmap[X][Y] == '.':
                twmap[X][Y] = twmap[x][y] + 1
                water.append([X,Y])

def move():
    while route:
        x,y = route.popleft()
        for i in range(4):
            X = x+dx[i]
            Y = y+dy[i]
            if 0 <= X < R and 0 <= Y < C:
                if twmap[X][Y] == 'D':
                    return twmap[x][y] + 1
                try:
                    if twmap[X][Y] > twmap[x][y]+1:
                        twmap[X][Y] = twmap[x][y] + 1
                        route.append([X,Y])
                except:
                    pass
    return 0

# for i in twmap:
#     print(*i)
flood()
# for i in twmap:
#     print(*i)
result = move()
# print('after move')
# for i in twmap:
#     print(*i)

if result == 0:
    print('KAKTUS')
else:
    print(result)

    
# flood = []
# spot = 0
# moving = dq([])
# for i in range(R):
#     for j in range(C):
#         if twmap[i][j] == '*':
#             flood.append(dq([[i,j]]))
#             spot += 1
#         elif twmap[i][j] == 'S':
#             moving.append([i,j])
#             twmap[i][j] = 1
#         elif twmap[i][j] == 'D':
#             bea = i
#             ver = j

# def move():
#     while moving:
#         if flood:
#             for j in range(spot):
#                 if flood[j]:
#                     cnt = len(flood[j])//len(moving) 
#                     for k in range(cnt):
#                         x,y = flood[j].popleft()
#                         for i in range(4):
#                             X = x+dx[i]
#                             Y = y+dy[i]
#                             if 0 <= X < R and 0 <= Y < C and twmap[X][Y] == '.':
#                                 twmap[X][Y] = '*'
#                                 flood[j].append([X,Y])

#         a,b = moving.popleft()
#         for i in range(4):
#             A = a+dx[i]
#             B = b+dy[i]
#             if 0 <= A < R and 0 <= B < C and twmap[A][B] == '.':
#                 twmap[A][B] = twmap[a][b] + 1
#                 moving.append([A,B])

# move()
# # for i in twmap:
# #     print(*i)

# result = 0
# for i in range(4):
#     BEA = bea + dx[i]
#     VER = ver + dy[i]
#     if 0 <= BEA < R and 0 <= VER < C:
#         try:
#             result = max(result,int(twmap[BEA][VER]))
#         except:
#             pass

# if result == 0:
#     print('KAKTUS')
# else:
#     print(result)





# #############################################
# # flood = dq([])
# # moving = dq([])
# # for i in range(R):
# #     for j in range(C):
# #         if twmap[i][j] == '*':
# #             flood.append([i,j])
# #         elif twmap[i][j] == 'S':
# #             moving.append([i,j])
# #             twmap[i][j] = 1
# #         elif twmap[i][j] == 'D':
# #             bea = i
# #             ver = j

# # def move():
# #     while moving:
# #         if flood:
# #             cnt = len(flood)//len(moving)  
# #             for j in range(cnt):
# #                 x,y = flood.popleft()
# #                 for i in range(4):
# #                     X = x+dx[i]
# #                     Y = y+dy[i]
# #                     if 0 <= X < R and 0 <= Y < C and twmap[X][Y] == '.':
# #                         twmap[X][Y] = '*'
# #                         flood.append([X,Y])
                        
                            

# #         a,b = moving.popleft()
# #         for i in range(4):
# #             A = a+dx[i]
# #             B = b+dy[i]
# #             if 0 <= A < R and 0 <= B < C and twmap[A][B] == '.':
# #                 twmap[A][B] = twmap[a][b] + 1
# #                 moving.append([A,B])
      

# # move()
# # for i in twmap:
# #     print(i)

# # result = 0
# # for i in range(4):
# #     BEA = bea + dx[i]
# #     VER = ver + dy[i]
# #     if 0 <= BEA < R and 0 <= VER < C:
# #         try:
# #             result = max(result,int(twmap[BEA][VER]))
# #         except:
# #             pass

# # if result == 0:
# #     print('KAKTUS')
# # else:
# #     print(result)






   