import sys
from collections import deque

N,M = map(int,input().split())
Map = [list(map(int,input().split())) for _ in range(N)]
visited = [[float('INF')]*M for _ in range(N)]


answer = float('inf')
sum = 0
dy = [-1,0,1]

def dfs(x,y,pd):
  global sum, answer
  if x == N-1: 
    answer = min(answer, sum)
  for d in dy : 
    if d!=pd and 0<=y+d<M and 0<=x+1<N:
      sum += Map[x+1][y+d]
      dfs(x+1,y+d,d)
      sum -= Map[x+1][y+d]

for i in range(M):
  sum+=Map[0][i]
  dfs(0,i,3)
  sum-=Map[0][i]


print(answer)


# def bfs():
#   q = deque()
#   for i in range(M):
#     q.append([0,i])
#     visited[0][i] = Map[0][i]
#   while(q):
#     x,y=q.popleft()
#     for d in dy:
#       if 0<=y+d<M and 0<=x+1<N:
#         w = visited[x][y] + Map[x+1][y+d]
#         if w < visited[x+1][y+d] :
#           visited[x+1][y+d] = w
#           q.append([x+1,y+d])
    
  
# bfs()
  
# print(visited)