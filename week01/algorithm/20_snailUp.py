import math

a,b,v = map(int,input().split())

# loc = 0
day = 0
# while loc < v:
#     loc = loc + a
#     if loc < v:
#         loc = loc - b
#     day = day + 1
day = math.ceil((v-a) / (a-b)) + 1
print(day)