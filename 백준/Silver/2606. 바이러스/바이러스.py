n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = []
def dfs(start):
    for next in graph[start]:
        if next != 1 and next not in visited:
            visited.append(next)
            dfs(next)

dfs(1)
print(len(visited))
