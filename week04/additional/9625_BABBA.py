K = int(input())
AB = [[0,0] for _ in range(K+1)]
AB[0] = [1,0]
for i in range(1,K+1):
    AB[i] = [AB[i-1][1],AB[i-1][0]+AB[i-1][1]]

print(*AB[K])

######2193 pinary num
K = int(input())
AB = [[0,0] for _ in range(K+1)]
AB[0] = [1,0]
for i in range(1,K+1):
    AB[i] = [AB[i-1][1],AB[i-1][0]+AB[i-1][1]]

print(sum(AB[K-1]))
