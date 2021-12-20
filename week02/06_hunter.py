import sys
M,N,L = map(int,sys.stdin.readline().split())
shoot = list(map(int,sys.stdin.readline().split()))
animal = []
for i in range(N):
    animal.append(sys.stdin.readline().split())
shoot.sort()
print(shoot,animal)
for i in range(N):
    animal[i]
#1차 시도
# blank = []
# shootrange = []


# for i in range(len(shoot)-1):
#     diff = shoot[i+1] - shoot[i]
#     if diff > L:
#         blank.append([i,shoot[i], shoot[i+1]])
#         shoot[i]+L
#         shoot[i]-L

# print(blank)