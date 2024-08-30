import sys
from collections import deque
n, m , v = map(int, sys.stdin.readline().split())

lst = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]

for x,y in lst: 
  graph[x].append(y)
  graph[y].append(x)

for i in graph:
  i.sort()

def bfs(start):
  visited = [start]
  q = deque()
  q.append(start)
  while(q):
    cur_v = q.popleft()
    for v in graph[cur_v]:
      if(v not in visited):
        visited.append(v)
        q.append(v)
  return visited

visited = []
def dfs(cur_v):
  visited.append(cur_v)
  for v in graph[cur_v]:
    if v not in visited:
      dfs(v)
  return visited


  
print(*dfs(v))
print(*bfs(v))
