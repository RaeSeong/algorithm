import sys
cnt = int(sys.stdin.readline())
for i in range(cnt):
    result = 0
    test = int(sys.stdin.readline())
    first = test//3
    rest = test%3
    second = first//2

    result = 3**first*rest
    print(result)

