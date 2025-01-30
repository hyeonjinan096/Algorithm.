from collections import deque

N,L,R = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
cnt = -1

dr = [[1,0],[0,1],[-1,0],[0,-1]]

def bfs(x,y,k):
    visited[x][y] = k
    lst = [graph[x][y]]
    q = deque([[x,y]])

    while(q):
        cx, cy = q.popleft()
        for dx,dy in dr:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and L <= abs(graph[cx][cy] - graph[nx][ny]) <= R:
                    lst.append(graph[nx][ny])
                    visited[nx][ny] = k
                    q.append([nx,ny])

    if len(lst) == 1:
        return graph[x][y]
    else:
        return sum(lst) // len(lst)


while(1):
    cnt+=1
    k = 1
    sum_dict = {}
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                sum_dict[k] = bfs(i,j,k)
                k+=1

    if k == N*N + 1:
        break

    for i in range(N):
        for j in range(N):
            graph[i][j] = sum_dict[visited[i][j]]

print(cnt)






