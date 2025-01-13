from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N)]

# 그래프 입력 처리
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(N):
        if lst[j] == 1:
            graph[i].append(j)

# 여행 경로 입력 처리
travel_route = [x - 1 for x in map(int, input().split())]

visited = [0] * N

def bfs(start):
    q = deque([start])
    visited[start] = 1

    while q:
        cur_x = q.popleft()
        for next_x in graph[cur_x]:
            if not visited[next_x]:
                visited[next_x] = 1
                q.append(next_x)

# 여행 경로 확인
# BFS를 수행하여 첫 번째 여행 경로에서 연결된 모든 노드를 방문
bfs(travel_route[0])

# 방문한 노드들 중에서 여행 경로에 포함되지 않은 노드가 있는지 확인
if all(visited[city] for city in travel_route):
    print("YES")
else:
    print("NO")
