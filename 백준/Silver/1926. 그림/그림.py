from collections import deque
N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

answer = [0,0]
dir = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(x,y):
  q = deque([[x,y]])
  cnt=1
  while(q):
    cx,cy = q.popleft()
    for dx,dy in dir:
      nx = cx+dx
      ny = cy+dy
      if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 1:
        graph[nx][ny] = 2
        cnt+=1
        q.append([nx,ny])

  return cnt
  
for i in range(N):
  for j in range(M):
    if graph[i][j] == 1:
      answer[0]+=1
      graph[i][j] = 2
      answer[1] = max(answer[1],bfs(i,j))

print(answer[0])
print(answer[1])
  
