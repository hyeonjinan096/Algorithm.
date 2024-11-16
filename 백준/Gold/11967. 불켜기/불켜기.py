import sys
from collections import deque
sys.setrecursionlimit(10**6)

N,M = map(int,sys.stdin.readline().split())
dic = {}
rooms = [[0]*N for _ in range(N)]
rooms[0][0] = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]
q = deque([])
answer = 1

for i in range(M):
  x,y,a,b = map(int,sys.stdin.readline().split())
  if (x-1,y-1) not in dic:
    dic[(x-1,y-1)] = []
  dic[(x-1,y-1)].append((a-1,b-1))

def visited_switch(x,y):
  global rooms,q,answer

  if (x,y) not in dic:
    return 
  for (i,j) in dic[(x,y)]:
    if rooms[i][j] == 0:
      rooms[i][j] = 1 
      answer+=1
      for k in range(4):
        ni = i+dx[k]
        nj = j+dy[k]
        if 0<=ni<N and 0<=nj<N and rooms[ni][nj] == 2:
          rooms[i][j] = 2
          q.append((i,j))
          break 

def bfs(x,y):
  global q
  rooms[x][y] = 2
  q.append((x,y))
  while(q):
    cx,cy = q.popleft()
    visited_switch(cx,cy)
    for i in range(4):
      nx = cx+dx[i]
      ny = cy + dy[i]
      if 0<=nx<N and 0<=ny<N and rooms[nx][ny] == 1:
        rooms[nx][ny] = 2
        q.append((nx,ny))

bfs(0,0)

print(answer)
#1-> 불켜진 방 + 방문할 수 있는 방
#2-> 방문한 방