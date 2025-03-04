n = int(input())
m = int(input())

graph = [[float('inf')]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = min(graph[a][b], c)

for i in range(1,n+1):
    graph[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j] if graph[i][j] != float('inf') else 0, end=" ")
    print()