n = 0
seq = 0
for i in range(9):
    k = int(input())
    if n < k:
        n = k
        seq = i+1
print(n)
print(seq)