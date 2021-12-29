from collections import deque
def solution(maps):
    answer = 0
    n = len(maps[0])
    m = len(maps)
    mapmove = [[-1]*n for _ in range(m)]

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    queue = deque()
    def bfs():
        cnt = 1
        while len(queue) > 1:
            if queue[0] == 0:
                queue.append(queue.popleft())
                cnt += 1
            x,y = queue.popleft()
            mapmove[x][y] = cnt
            if x == n-1 and y == m-1:
                return mapmove[x][y]
            for i in range(4):
                X = x+dx[i]
                Y = y+dy[i]
                if 0<=X<m and 0<=Y<n and maps[X][Y] == 1 and mapmove[X][Y] == -1:
                    queue.append([X,Y])
        return -1

    queue.append([0,0])
    queue.append(0)
    answer = bfs()

    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))