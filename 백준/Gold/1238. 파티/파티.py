#3:35
import sys
from heapq import heappop, heappush

N,M,X = map(int,sys.stdin.readline().split())

dic = [[] for _ in range(N)]
rev_dic = [[] for _ in range(N)]

for _ in range(M):
  a,b,d = map(int,sys.stdin.readline().split())
  a,b = a-1, b-1
  dic[a].append([b,d])
  rev_dic[b].append([a,d])
    
def dijkstra(s, dic):
  q = []
  result = [float('INF')]*N
  heappush(q, (0,s))
  result[s] = 0
  while(q):
    cd, cx = heappop(q)
    for nx, nd in dic[cx]:
      if result[nx] > cd + nd:
        result[nx] = cd+nd
        heappush(q,(cd+nd,nx)) 
  return result


back = dijkstra(X-1, dic)
go = dijkstra(X-1, rev_dic)
answer = 0
for i in range(len(go)):
  answer = max(answer,go[i]+back[i])

print(answer)

    
    
    
    

    

