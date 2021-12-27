import heapq
def solution(jobs):
    answer = 0
    jobs.sort(key = lambda x:x[0])
    alltime = jobs[0][1] - jobs[0][0]
    done = jobs[0][1]
    wait = []
    for i in range(1,len(jobs)):
        if jobs[i][0] < done:
            heapq.heappush(wait,(jobs[i][1],jobs[i][0]))
        else:
            if wait:
                need,start = heapq.heappop(wait)
                heapq.heappush(wait,(jobs[i][1],jobs[i][0]))
            else:
                need,start = jobs[i][0], jobs[i][1]
            done = jobs[i][0] + need
            alltime += done - start
    while wait:
        need,start = heapq.heappop(wait)
        done += need
        alltime += done - start
    answer = alltime // len(jobs)
    return answer

print(solution([[0, 3], [1, 9], [2, 6]]))