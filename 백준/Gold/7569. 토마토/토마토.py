from collections import deque
M,N,H = map(int,input().split())

#정보 받기
graph = []
for i in range(H):
  graph.append([list(map(int,input().split())) for _ in range(N)])

dir = [[0,1,0],[0,-1,0],[0,0,1],[0,0,-1],[1,0,0],[-1,0,0]]
def bfs():
  answer = 0
  q = deque([])
  for i in range(H):
    for j in range(N):
      for k in range(M):
        if graph[i][j][k] == 1:
          q.append([i,j,k,0])
  while(q):
    h,n,m,c = q.popleft()
    answer = max(answer,c)
    for dh,dn,dm in dir:
      nh = h+dh
      nn = n+dn
      nm = m+dm
      if 0<=nh<H and 0<=nn<N and 0<=nm<M:
        if graph[nh][nn][nm] == 0:
          graph[nh][nn][nm] = 1
          q.append([nh,nn,nm,c+1])
  
  for i in range(H):
    for j in range(N):
      for k in range(M):
        if graph[i][j][k] == 0:
          return -1
  return answer

print(bfs())


