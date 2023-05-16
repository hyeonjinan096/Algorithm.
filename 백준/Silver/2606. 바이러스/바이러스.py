import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph=[[] for _ in range(n+1)]

visited=[]
def dfs(cur_v):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if(v not in visited):
            dfs(v)
    return len(visited)-1

for i in range(m):
    a, b = map(int,sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

print(dfs(1))