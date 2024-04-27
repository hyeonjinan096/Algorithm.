#2:07
from collections import deque

n = int(input())
x,y = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

def bfs(start_v):
    visited=[start_v]
    q = deque()
    q.append((start_v,0))
    while(q):
        cur_v, c = q.popleft()
        if cur_v == y:
            return c
        for cur_v in graph[cur_v]:
            if cur_v not in visited:
                visited.append(cur_v)
                q.append((cur_v,c+1))
    return -1

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(x))