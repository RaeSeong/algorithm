import sys
K = int(sys.stdin.readline())
money = [int(sys.stdin.readline()) for _ in range(K)]
account = []
for i in money:
    if i == 0:
        account.pop()
    else:
        account.append(i)

print(sum(account))