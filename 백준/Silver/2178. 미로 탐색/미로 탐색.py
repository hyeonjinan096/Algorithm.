import sys
from collections import deque

r,c = map(int, sys.stdin.readline().strip().split())

graph = []
visited=[[False]*c for _ in range(r)]
for i in range(r):
    graph.append(list(map(int,sys.stdin.readline().strip())))


dx = [1,-1,0,0]
dy = [0,0,1,-1]

visited[0][0]=True
q=deque()
q.append((0,0,1))
f=0
while(q):
    cx,cy,count = q.popleft()
    for i in range(4):
        nx =cx+dx[i]
        ny = cy+dy[i]
        if(nx>=0 and nx < r and ny>=0 and ny <c):
            if(graph[nx][ny]==1 and not visited[nx][ny]):
                if(nx == r-1 and ny ==c-1):
                    print(count+1)
                    f=1
                    break
                visited[nx][ny]=True
                q.append((nx,ny,count+1))
    if(f==1):
        break

