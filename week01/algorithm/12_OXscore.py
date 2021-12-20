a = int(input())
for i in range(a):
    ox = input()
    score = 0
    sum = 0
    for j in list(ox):
        if j == 'O':
            score = score + 1
            sum = sum + score
        else:
            score = 0
    print(sum)