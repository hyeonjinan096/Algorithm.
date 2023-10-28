a = []
n,m = map(int,input().split())
for i in range(n):
    a.append(list(map(int,input().split())))

b = []
m,k = map(int,input().split())
for i in range(m):
    b.append(list(map(int,input().split())))

c = [] 
for i in range(n):
    c.append([])
    for j in range(k): 
        temp = 0
        for l in range(m):
            temp += a[i][l] * b[l][j]
        c[i].append(temp)

for i in c:
    print(*i)