from heapq import heappop, heappush
N,M = map(int,input().split())
graph = [list(input()) for _ in range(N)]
values = [[(0,0)]*M for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = [[0]*M for _ in range(N)]

def isOk(x,y):
  if 0<=x<N and 0<=y<M:
    return True
  return False

for i in range(N):
  for j in range(M):
    if graph[i][j] == 'F':
      start = (i,j)
    elif graph[i][j] == 'S':
      end = (i,j)
    elif graph[i][j] == 'g':
      values[i][j] = (1,0)
    else:
      for d in range(4):
        if isOk(i+dx[d], j+dy[d]):
          if graph[i+dx[d]][j+dy[d]] == 'g':
            values[i][j] = (0,1)
            break

def dijkstra():
  x,y = start
  q = []
  heappush(q,(0, 0, x,y))
  visited[x][y] = 1

  while(q):
    g,f,cx,cy = heappop(q)

    if (cx,cy) == end:
      return g,f

    for d in range(4):
      nx = cx + dx[d]
      ny = cy + dy[d]
      if isOk(nx,ny) and not visited[nx][ny]:
        visited[nx][ny] = 1
        ng, nf = values[nx][ny]
        heappush(q,(g+ng,f+nf,nx,ny))


print(*dijkstra())




#쓰레기통과 쓰레기 옆 통과

