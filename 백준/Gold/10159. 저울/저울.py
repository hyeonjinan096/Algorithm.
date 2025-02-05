import sys

INF = int(1e9)
n = int(sys.stdin.readline())  # 물건의 개수
m = int(sys.stdin.readline())  # 측정된 물건의 쌍
# 2차원 그래프, 모든 값을 무한으로 초기화

graph = [[INF] * (n + 1) for _ in range(n + 1)]   # 거리를 담는 테이블

# 1. 자기 자신으로 가는 노드 비용을 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 1

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1

# 2. 플로이드와셜 점화식 - a에서 b로 가는 경로가 있는지 확인 
for k in range(1, n + 1):
    for a in range(1, n + 1):   # 출발 노드
        for b in range(1, n + 1):   # 도착 노드
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 3. a, b 비교 가능한지 확인 
for a in range(1, n + 1):
    count = 0
    for b in range(1, n + 1):
        if graph[a][b] == INF and graph[b][a] == INF:  # a>b, b>a 가는 경로가 없는 경우 + 1
            count += 1
    print(count)