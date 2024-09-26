import sys
sys.setrecursionlimit(10**9)

N, M, K = map(int,input().split())
value = [list(map(int,input().split())) for _ in range(K)]
graph = [[0]*M for _ in range(N)]
for x,y in value:
  graph[x-1][y-1] = 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

Max =0
cnt = 0

def dfs(x,y):
  global cnt
  graph[x][y] = 2
  cnt+=1
  for i in range(4):
    n_x = x+dx[i]
    n_y = y+dy[i]
    if 0<=n_x<N and 0<=n_y<M and graph[n_x][n_y] == 1:
      dfs(n_x,n_y) 

for x in range(N):
  for y in range(M):
    if graph[x][y] == 1:
      cnt = 0
      dfs(x,y)
      if Max < cnt:
        Max = cnt

print(Max)