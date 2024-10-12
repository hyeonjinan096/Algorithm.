from collections import deque

N,M,X = map(int,input().split())
graph = [[] for _ in range(N)]
rev_graph = [[] for _ in range(N)]
go =[float('inf')]*(N)
back = [float('inf')]*(N)
X-=1
go[X] = 0
back[X] = 0

for _ in range(M):
  x,y,t = map(int,input().split())
  x,y = x-1,y-1
  graph[x].append((y,t))
  rev_graph[y].append((x,t))

def bfs(s, arr, value):
  q = deque([(s,0)])
  while(q):
    nx,nt = q.popleft()
    for x,t in arr[nx]:
      if value[x] > nt+t:
        value[x] = nt+t
        q.append((x,nt+t))

bfs(X,rev_graph, go)
bfs(X,graph, back)

answer = []
for i in range(len(go)):
  answer.append(go[i]+back[i])
print(max(answer))
      