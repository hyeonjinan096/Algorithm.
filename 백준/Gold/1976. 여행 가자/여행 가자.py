# 유니온 파인드 함수 정의
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x

# 입력 처리
N = int(input())
M = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
travel_route = list(map(int, input().split()))

# 유니온 파인드 초기화
parent = [i for i in range(N)]

# 그래프를 기반으로 연결된 도시들을 병합
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            union(parent, i, j)

# 여행 경로의 모든 도시가 같은 집합인지 확인
root = find(parent, travel_route[0] - 1)  # 첫 번째 도시의 루트
if all(find(parent, city - 1) == root for city in travel_route):
    print("YES")
else:
    print("NO")
