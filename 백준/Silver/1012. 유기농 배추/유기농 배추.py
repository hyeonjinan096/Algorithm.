import sys
sys.setrecursionlimit(10000)

import sys

T = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
  graph[x][y] = 2
  for i in range(4):
    cur_x, cur_y =x+dx[i],y+dy[i]
    if 0<=cur_x<M and 0<=cur_y<N and graph[cur_x][cur_y]==1:
      graph[x][y] = 2
      dfs(cur_x,cur_y)
  return
    



for _ in range(T):
  M,N,K = map(int,input().split())
  graph = [[0]*N for _ in range(M)]
  answer = 0

  for j in range(K):
    x,y = map(int,input().split())
    graph[x][y] = 1
  
  for i in range(M):
    for j in range(N):
      if graph[i][j] == 1:
        dfs(i,j)
        answer+=1

  print(answer)
