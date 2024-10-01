#3:15
from collections import deque

N,M,X = map(int,input().split())
go = [float("inf")]*(N+1)
back = [float("inf")]*(N+1)
go[0],back[0] = 0,0
dic = {}
rev_dic = {}

for _ in range(M):
  x,y,t = map(int, input().split())
  if x not in dic:
    dic[x] = []
  dic[x].append((y,t))

  if y not in rev_dic:
    rev_dic[y] = []
  rev_dic[y].append((x,t))

def bfs(x,dic,value):
  q = deque([x])
  value[x] = 0
  
  while(q):
    cx = q.popleft()
    for y,t in dic[cx]:
      if value[y] > value[cx]+t:
        value[y] = value[cx]+t
        q.append(y)
  
bfs(X, rev_dic, go)
bfs(X, dic, back)
answer = 0
for i in range(N+1):
  answer = max(answer, go[i]+back[i])
print(answer)