import heapq

def solution(operations):
    answer = []
    minheap = []
    maxheap = []
    heaplen = 0
    for i in operations:
        print(minheap,maxheap,heaplen)
        command, val = i.split()
        if command == 'I':
            heapq.heappush(minheap,int(val))
            heapq.heappush(maxheap,-int(val))
            heaplen += 1
        else:
            if heaplen == 0:
                continue
            else:
                if val == '-1':
                    heapq.heappop(minheap)
                else: 
                    heapq.heappop(maxheap)
                heaplen -= 1
        if heaplen == 0:
            minheap = []
            maxheap = []
    if heaplen > 0:
        answer = [-heapq.heappop(maxheap),heapq.heappop(minheap)]
    else:
        answer = [0,0]
    return answer

# print(solution(["I 16","D 1"]))
# print(solution(["I 7","I 5","I -5","D -1"]))
print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))