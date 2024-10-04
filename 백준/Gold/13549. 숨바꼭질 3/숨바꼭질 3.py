from collections import deque

N, K = map(int,input().split())
visited = [float('inf')]* 100001
def bfs():
  q = deque([K])
  visited[K] = 0

  while(q):
    x = q.popleft()
    cost = visited[x]
    if x == N:
      return cost
    
    if 0<=x-1<=100000 and cost+1 < visited[x-1]:
      q.append(x-1)
      visited[x-1] =cost +1
    if 0<=x+1<=100000 and cost+1 <  visited[x+1]:
      q.append(x+1)
      visited[x+1] = cost +1
    if x%2 == 0 and 0<=x//2<=100000 and cost < visited[x//2]:
      q.append(x//2) 
      visited[x//2] = cost 

print(bfs())


# bfs visited 위치 
# visited 체크 
