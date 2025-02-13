R,C,T = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

direction = [[(-1,0),(0,1),(1,0),(0,-1)], [(1,0),(0,1),(-1,0),(0,-1)]]
direction2 = [(1,0),(-1,0),(0,1),(0,-1)]

def spread():
    global graph
    new_graph = [[0 for _ in range(C)]  for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0 :
                n = graph[i][j] // 5
                for dx, dy in direction2:
                    nx = i + dx
                    ny = j + dy
                    if 0<=nx<R and 0<=ny<C and graph[nx][ny] != -1:
                        new_graph[nx][ny] += n
                        graph[i][j] -= n
            new_graph[i][j] += graph[i][j]
    graph = new_graph

def air(X,Y,D):
    dir = direction[D]
    x = X + dir[0][0]
    y = Y + dir[0][1]
    i = 0
    graph[x][y] = 0
    while(1):
        if (D == 0 and x+dir[i][0] > X) or (D == 1 and x+dir[i][0] < X) or not (0<= x + dir[i][0] < R) or not (0<= y + dir[i][1]<C) :
            i+=1

        nx = x + dir[i][0]
        ny = y + dir[i][1]

        if nx == X and ny == Y:
            graph[x][y] = 0
            break

        graph[x][y] = graph[nx][ny]
        x = nx
        y = ny

up = []
down = []
for i in range(R):
    if graph[i][0] == -1:
        up = [i,0]
        down = [i+1,0]
        break

for _ in range(T):
    spread()
    air(up[0],up[1],0)
    air(down[0],down[1],1)


answer = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            continue
        answer += graph[i][j]
print(answer)