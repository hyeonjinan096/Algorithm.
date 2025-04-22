n = int(input())
lst = list(map(int, input().split()))

tree = [[] for _ in range(n)]
for i in range(n):
    if lst[i] != -1:
        tree[lst[i]].append(i)

def dfs(node):
    times = []
    for child in tree[node]:
        times.append(dfs(child))
    times.sort(reverse=True)  # 시간이 큰 순서대로 전파

    max_time = 0
    for idx, t in enumerate(times):
        max_time = max(max_time, t + idx + 1)  # 전파 순서 +1초

    return max_time

root = lst.index(-1)
print(dfs(root))
