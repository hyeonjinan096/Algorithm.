from collections import deque
M,N = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

dir = [(1,0),(0,1),(-1,0),(0,-1)]
answer = 0

def bfs():
    global answer
    q = deque([]) 
    for x in range(N):
        for y in range(M):
            if graph[x][y] == 1:
                q.append([x,y,0])
    while(q):
        cx,cy,day = q.popleft()
        answer = max(answer,day)
        for [dx,dy] in dir:
            nx = cx+ dx
            ny = cy+ dy
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append([nx,ny,day+1])
    
bfs()
flag = 1
for x in range(N):
    for y in range(M):
        if graph[x][y] == 0:
            flag = 0
            break
    if flag == 0:
        break

if flag:
    print(answer)
else:
    print(-1)

