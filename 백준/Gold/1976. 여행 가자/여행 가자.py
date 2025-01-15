def union(x,y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

N = int(input())
M = int(input())
parent = [i for i in range(N)]
for i in range(N):
    lst = list(map(int,input().split()))
    for j in range(N):
        if lst[j] == 1:
            union(i,j)

route = [x-1 for x in map(int,input().split())]

start = parent[route[0]]
for i in range(M):
    if parent[route[i]] != start:
        print("NO")
        break
else:
    print("YES")


