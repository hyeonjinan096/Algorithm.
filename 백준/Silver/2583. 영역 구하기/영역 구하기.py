from collections import deque

M,N,K = map(int,input().split())
graph = [[0]*M for _ in range(N)]

for i in range(K):
  x,y,x2,y2 = map(int,input().split())
  x2,y2 = x2-1, y2-1
  for i in range(x,x2+1):
    for j in range(y,y2+1):
      graph[i][j] = 1

dir = [[1,0],[0,1],[-1,0],[0,-1]]
def bfs(x,y):
  cnt = 1
  q = deque([[x,y]])
  while(q):
    cx,cy = q.popleft()
    for dx,dy in dir:
      nx = cx+dx
      ny = cy+dy
      if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0:
        cnt+=1
        graph[nx][ny] =2
        q.append([nx,ny])
  return cnt

answer = 0
arr = []
for i in range(N):
  for j in range(M):
    if graph[i][j] == 0:
      graph[i][j] = 2
      arr.append(bfs(i,j))
      answer+=1

arr.sort()
print(answer)
print(*arr)





  