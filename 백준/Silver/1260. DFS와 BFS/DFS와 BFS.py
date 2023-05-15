import sys
from collections import deque

N,M,V = map(int,sys.stdin.readline().strip().split())

graph =[[] for _ in range(N+1)]

def dfs(cur_v):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if(v not in visited):
            dfs(v)
    return visited    

def bfs(start_v):
    visited=[start_v]
    q = deque() 
    q.append(start_v)
    while(q):
        cur_v =q.popleft()
        for v in graph[cur_v]:
            if(v not in visited):
                visited.append(v)
                q.append(v)
    return visited




for i in range(M):
    a,b = map(int,sys.stdin.readline().strip().split())
    #if(a not in graph): graph[a]=list()
    #if(b not in graph): graph[b]=list()
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited=[]
print(*dfs(V))
visited = [False]*(N+1)
print(*bfs(V))
