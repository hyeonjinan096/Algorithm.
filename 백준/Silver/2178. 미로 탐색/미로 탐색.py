from collections import deque

n,m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
x = [0,0,1,-1]
y = [1,-1,0,0]
def bfs(start_x, start_y):
    visited[start_x][start_y] = 1
    q = deque()
    q.append((start_x,start_y))
    while(q):
        cur_x, cur_y = q.popleft()
        for i in range(4):
            next_x = cur_x + x[i]
            next_y = cur_y + y[i]
            if 0 <= next_x < n and 0 <= next_y <m:
                if visited[next_x][next_y] == 0 and graph[next_x][next_y] == 1:
                    visited[next_x][next_y] = visited[cur_x][cur_y] +1
                    q.append((next_x,next_y))
bfs(0,0)
print(visited[n-1][m-1])