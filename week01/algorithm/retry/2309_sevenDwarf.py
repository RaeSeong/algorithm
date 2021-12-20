import sys
dwarfs = [int(sys.stdin.readline()) for _ in range(9)]
fake_sum = sum(dwarfs) - 100
done = False
for i in range(8):
    for j in range(i+1,9):
        if dwarfs[i] + dwarfs[j] == fake_sum:
            fake_a = dwarfs[i]
            fake_b = dwarfs[j]
            dwarfs.remove(fake_a)
            dwarfs.remove(fake_b)
            done = True
            break
    if done == True:
        break
dwarfs.sort()

for i in dwarfs:
    print(i)