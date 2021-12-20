import sys
N = int(sys.stdin.readline())
schedule = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
benefit = [0]*(N+1)

for i in range(1,N+1):
    if schedule[N-i][0] > i:
        if i > 1:
            benefit[N-i] = benefit[N-i+1]
        continue
    benefit[N-i] = max(benefit[N-i+1],benefit[N-i+schedule[N-i][0]]+schedule[N-i][1])

print(benefit[0])

# ing = [0,0]
# for i in range(N):
#     if schedule[i][0] > N-i:
#         benefit[i] = benefit[i-1]
#         continue
#     if ing[1] > 0:
#         if benefit[i-1] >= benefit[i-(ing[0]-ing[1])-1] + schedule[i][1]:
#             benefit[i] = benefit[i-1]
#         else:
#             benefit[i] = benefit[i-(ing[0]-ing[1])-1] + schedule[i][1]
#             ing[0] = schedule[i][0]
#             ing[1] = schedule[i][0]
#     else:
#         benefit[i] = benefit[i-1] + schedule[i][1]
#         ing[0] = schedule[i][0]
#         ing[1] = schedule[i][0]
#     ing[1] -= 1

# print(benefit[N-1])