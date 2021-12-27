import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    first = 0
    second = 0
    while scoville[0] < K and len(scoville) > 1:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        fusion = first + second*2
        heapq.heappush(scoville, fusion)
        answer += 1
    if scoville:
        first = scoville.pop()
    if first < K:
        return -1
    return answer

print(solution([12,10,9,3,2,1], 7))