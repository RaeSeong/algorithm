def solution(prices):
    answer = [0]*len(prices)
    stack = []
    for idx, price in enumerate(prices):
        while stack:
            start, val = stack.pop()
            if val > price:
                answer[start] = idx - start
            else:
                stack.append([start,val])
                break
        stack.append([idx,price])
    while stack:
        start, val = stack.pop()
        answer[start] = len(prices)-1 - start

    return answer

print(solution([1, 2, 3, 2, 3]))