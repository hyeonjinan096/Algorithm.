import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split(' '))
graph = [list(map(int,sys.stdin.readline().split(' '))) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
start = [0,0]

dir = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs(start):
  q = deque([start])
  while(q):
    cx,cy = q.popleft()
    for [dx,dy] in dir:
      nx = cx+dx
      ny = cy+dy
      if nx <0 or nx>=n or ny<0 or ny>=m:
        continue
      if graph[nx][ny] == 0:
        continue
      elif graph[nx][ny] == 1 and (visited[nx][ny] > visited[cx][cy]+1 or visited[nx][ny]==-1):
        visited[nx][ny] = visited[cx][cy]+1
        q.append([nx,ny])


for i in range(n):
  for j in range(m):
    if graph[i][j] == 2:
      visited[i][j] = 0
      start = [i,j]
    elif graph[i][j] == 0:
      visited[i][j] = 0
      
bfs(start)
for data in visited:
  print(*data)