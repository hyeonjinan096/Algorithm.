# 쓰레기 정보 저장 배열 
# 방문 최적 쓰레기 정보 저장 dictionary dic[(x,y)] = (a,b)
# heapq.heappush(value, (a,b,x,y))
#1:23
import heapq

N,M = map(int,input().split())
graph =[ list(input()) for _ in range(N)]
costs = {}
dx =[0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,1,-1,-1,1]


for i in range(N):
  for j in range(M):
    if graph[i][j] == "F":
      flower = (i,j)
    elif graph[i][j] == "S":
       start= (i,j)

def check(x,y):
  global N,M
  if x == flower[0] and y == flower[1]:
    return (0,0)
  if graph[x][y] == "g":
    return (1,0)
  for i in range(4):
    if 0<=x+dx[i]<N and 0<=y+dy[i]<M:
      if graph[x+dx[i]][y+dy[i]] == "g":
        return(0,1)
  return (0,0)


def dijkstra():
  q = []
  heapq.heappush(q,(0,0,start[0],start[1]))
  costs[start] = (0,0)
  while(q):
    a,b,x,y = heapq.heappop(q)
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      if 0<=nx<N and 0<=ny<M and (nx,ny) not in costs:
        i,j = check(nx,ny)
        costs[(nx,ny)] = (a+i, b+j)
        heapq.heappush(q,(a+i,b+j,nx,ny))

dijkstra()
print(*costs[flower])