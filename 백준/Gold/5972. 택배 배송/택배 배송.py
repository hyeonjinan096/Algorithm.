import heapq

N,M = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    x,y,z = map(int,input().split())
    x-=1
    y-=1
    graph[x].append([y,z])
    graph[y].append([x,z])

visited = [float('inf')]*N
def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    visited[start] = 0

    while(q):
        cnt, x = heapq.heappop(q)
        for next_x, next_cnt in graph[x]:
            new_cnt = cnt+next_cnt
            if new_cnt < visited[next_x]:
                visited[next_x] = new_cnt
                heapq.heappush(q,(new_cnt, next_x))

    return visited[N-1]

print(dijkstra(0))