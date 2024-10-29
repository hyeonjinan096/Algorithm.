import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
  N, M, K = map(int,sys.stdin.readline().split())
  graph = [[0]*M for _ in range(N)]

  for _ in range(K):
    x,y = map(int,sys.stdin.readline().split())
    graph[x][y] = 1

  dic = [(0,1),(0,-1),(1,0),(-1,0)]

  def bfs(start):
    q = deque([start])
    while(q):
      cx, cy = q.popleft()
      for dx, dy in dic:
        nx = cx+dx
        ny = cy+dy
        if 0<=nx<N and 0<=ny<M and graph[nx][ny] ==1:
          graph[nx][ny] = 2
          q.append([nx,ny])


  answer = 0
  for i in range(N):
    for j in range(M):
      if graph[i][j] == 1:
        graph[i][j] = 2
        bfs([i,j])
        answer +=1

  print(answer)