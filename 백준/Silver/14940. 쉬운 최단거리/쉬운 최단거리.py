import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]

for i in range(N):
  for j in range(M):
    if graph[i][j] == 2:
      S = [i,j]
      visited[i][j] = 0
    if graph[i][j] == 0:
      visited[i][j] = 0

dir = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(S):
  q = deque([[S[0],S[1]]])
  while(q):
    x,y = q.popleft()
    for dx,dy in dir:
      nx = x+dx
      ny = y+dy
      if 0<=nx<N and 0<=ny<M:
        if graph[nx][ny] == 0:
          continue
        if visited[nx][ny]==-1 or visited[nx][ny] > visited[x][y]+1:
          visited[nx][ny] = visited[x][y]+1
          q.append([nx,ny])
    
bfs(S)

for v in visited:
  print(*v)