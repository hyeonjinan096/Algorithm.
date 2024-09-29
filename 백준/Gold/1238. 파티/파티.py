from collections import deque

N,M,X = map(int,input().split())
X -=1
dic = {}
rev_dic = {}
go = [float("inf")]*N
back = [float("inf")]*N
go[X] = 0
back[X] = 0

for _ in range(M):
  a,b,t = map(int,input().split())
  a-=1
  b-=1
  if not a in dic:
    dic[a] = []
  dic[a].append((b,t))
  if not b in rev_dic:
    rev_dic[b] = []
  rev_dic[b].append((a,t))

  
def bfs(s, dic, value):
  q = deque([(s,0)])
  while(q):
    cs, ct = q.popleft()
    for e,t in dic[cs]:
      if value[e] > ct+t:
        value[e] = ct+t
        q.append((e,ct+t))
      
bfs(X, rev_dic, go)
bfs(X, dic, back)

answer = []
for i in range(len(go)):
  answer.append(go[i] + back[i])

print(max(answer))
      

