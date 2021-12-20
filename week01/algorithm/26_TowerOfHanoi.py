import sys

def TOH(N,start,end):
    if N > 0:
        TOH(N-1,start,6-start-end)
        # print(start,end)
        print(start,end)
        TOH(N-1,6-start-end,end)
        
data = int(sys.stdin.readline())

if data > 20:
    print(2**data - 1)
else:
    print(2**data - 1)
    TOH(data,1,3)

# def TOH(N,start,end):
#     if N > 1:
#         TOH(N-1,start,6-start-end)
    
#     list.append([start,end])

#     if N > 1:
#         TOH(N-1,6-start-end,end)
        
# data = int(sys.stdin.readline())

# if data > 20:
#     print(data**2 - 1)
# else:
#     list = []
#     TOH(data,1,3)
#     print(len(list))

#     for i in range(len(list)):
#         print(list[i][0],list[i][1])

