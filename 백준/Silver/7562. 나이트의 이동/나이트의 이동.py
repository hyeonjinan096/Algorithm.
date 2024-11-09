from collections import deque
T = int(input())

dir = [(-2,-1),(-1,-2),(-2,1),(-1,2),(1,2),(2,1),(1,-2),(2,-1)]

for _ in range(T):
    N = int(input())
    graph = [[float('inf')]*N for _ in range(N)]

    x,y = map(int,input().split(' '))
    tx,ty = map(int,input().split(' '))
    
    def bfs(x,y):
        q = deque([[x,y]])
        graph[x][y] = 0

        while(q):
            cx,cy = q.popleft()
            cost = graph[cx][cy]
            for dx,dy in dir:
                nx = cx+dx
                ny = cy+dy
                if 0<=nx<N and 0<=ny<N and graph[nx][ny] > cost + 1:
                    graph[nx][ny] = cost+1
                    q.append([nx,ny])

    bfs(x,y)
    
    print(graph[tx][ty])

