n = int(input())
graph = [list(map(int,input().split())) for i in range(n)]
values = [[0]*n for _ in range(n)]
for i in range(5):
    for j in range(n):
        for k in range(j+1,n):
            if graph[j][i] == graph[k][i]:
                values[k][j] = 1
                values[j][k] = 1

cnt = []
for i in values:
    cnt.append(i.count(1))
print(cnt.index(max(cnt))+1)