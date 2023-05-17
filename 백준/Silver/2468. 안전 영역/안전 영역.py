import sys  #1:12
from collections import deque
N = int(sys.stdin.readline().strip())
graph=[]
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().strip().split())))

visited=[[False]*N for _ in range(N)]

def bfs(x,y,h):
     dx=[-1,1,0,0]
     dy=[0,0,-1,1]
     visited[x][y]=True
     q= deque()
     q.append((x,y))
     while(q):
          cx ,cy =q.popleft()
          for i in range(4):
               nx = cx + dx[i]
               ny = cy + dy[i]
               if(nx>=0 and nx <N and ny>=0 and ny<N):
                    if(graph[nx][ny]>h and not visited[nx][ny]):
                         visited[nx][ny]=True
                         q.append((nx,ny))
          
          
    
def count(h):
     #함수안에서 visited초기화 했더니 지역변수처럼 된 거 같다.
     c=0
     for i in range(N):
          for j in range(N):
               if(graph[i][j]>h and not visited[i][j]):
                bfs(i,j,h)
                c+=1
     return c

Max =0  #max로 썼다가 max()와 연결되면서 오류 발생 (나중에 정리할 거 파일에 있음 정리할 것)
max_H =max(map(max,graph))  #이중배열 max값 구하기 정리
for h in range(max_H+1):    #범위를 그냥 N+1로 두었다가 틀림
      visited=[[False]*N for _ in range(N)]
      k = count(h)
      if(Max < k):
           Max = k

print(Max)