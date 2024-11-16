#단지수
#단지에 속하는 집의 수
from collections import deque

N = int(input())
graph = [list(input()) for _ in range(N)]

dir = [[1,0],[-1,0],[0,1],[0,-1]]
def bfs(x,y):
  q = deque([[x,y]])
  cnt = 1
  while(q):
    cx,cy = q.popleft()
    for dx,dy in dir:
      nx = cx+dx 
      ny = cy+dy
      if 0<=nx<N and 0<=ny<N and graph[nx][ny] == '1':
        graph[nx][ny] = '2'
        cnt+=1
        q.append([nx,ny])
  return cnt

answer_cnt = 0
answer = []

for i in range(N):
  for j in range(N):
    if graph[i][j] == '1':
      answer_cnt+=1
      graph[i][j] = '2'
      answer.append(bfs(i,j))

answer.sort()
print(answer_cnt)
for a in answer:
  print(a)