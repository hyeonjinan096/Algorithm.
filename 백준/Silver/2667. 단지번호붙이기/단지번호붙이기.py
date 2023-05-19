import sys
from collections import deque
N = int(sys.stdin.readline().strip())

graph =[]
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().strip())))
visited =[[False]*N for _ in range(N)]

def bsq(x,y,c):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    visited[x][y] = True
    q = deque()
    q.append((x,y))
    while(q):
        cx,cy = q.popleft()
        for i in range(4):
            nx = cx +dx[i]
            ny = cy +dy[i]
            if(nx>=0 and nx<N and ny>=0 and ny<N):
                if(graph[nx][ny]==1 and not visited[nx][ny]):
                    visited[nx][ny]=True
                    q.append((nx,ny))
                    c+=1
    return c

count =0
arr=[]

for i in range(N):
    for j in range(N):
        if(graph[i][j]==1 and not visited[i][j]):
            arr.append(bsq(i,j,1))
            count+=1


arr.sort()
print(count)
for i in arr:
    print(i)


