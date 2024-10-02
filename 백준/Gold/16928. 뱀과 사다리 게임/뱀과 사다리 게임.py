from collections import deque
N,M = map(int,input().split())
dic = {}
for _ in range(N+M):
  x,y = map(int,input().split())
  dic[x] = y

board = [float("inf")]*101
visited = [0]*101
answer = float("inf")

def bfs():
  global answer
  q = deque([1])
  board[1] = 0
  visited[1] = 1

  while(q):
    cx = q.popleft()
    if cx == 100:
      answer =  min(answer, board[cx])
      break
    for i in range(1,7):
       nx = cx+i
       if 0<nx<101 and not visited[nx]:
        if nx in dic:
            nx = dic[nx]
        if not visited[nx]:
            visited[nx] = 1
            board[nx] = board[cx]+1
            q.append(nx)

bfs()
print(answer)