import sys
sys.setrecursionlimit(10000)

T = int(input())
dx=[0,0,-1,1]
dy = [1,-1,0,0]

for _ in range(T):
  answer =0
  M,N,K = map(int,input().split())
  graph = [[0]*M for _ in range(N)]
  for _ in range(K):
    y,x = map(int,input().split())
    graph[x][y] = 1
  
  def dfs(x,y):
    graph[x][y] = 2
    for i in range(4):
      if 0<=x+dx[i]<N and 0<=y+dy[i]<M:
        if graph[x+dx[i]][y+dy[i]] == 1:
          dfs(x+dx[i], y+dy[i])

  for i in range(N):
    for j in range(M):
      if graph[i][j] ==1:
        dfs(i,j)
        answer +=1
  print(answer)
      
