import sys
from collections import deque

N,M = map(int,input().split(' '))
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dir = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]


def bfs(x,y):
  q = deque([[x,y]])
  while(q):
    x,y = q.popleft()
    for dx,dy in dir:
      nx = x + dx
      ny = y + dy
      if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and graph[nx][ny]:
        visited[nx][ny] = 1
        q.append([nx,ny])

answer = 0

for i in range(N):
  for j in range(M):
    if not visited[i][j] and graph[i][j]:
      visited[i][j] = 1
      bfs(i,j)
      answer+=1

print(answer)
      
