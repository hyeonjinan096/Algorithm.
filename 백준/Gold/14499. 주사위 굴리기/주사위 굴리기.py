import sys
input = sys.stdin.readline

N,M,x,y,k= map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
orders = list(map(int,input().split()))

dice = [0]*6
dir = [[],[0,1],[0,-1],[-1,0],[1,0]]

def move(x,y,n):
    global dice
    if n == 1:
        dice = [dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
    elif n == 2:
        dice = [dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
    elif n == 3:
        dice = [dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
    elif n == 4:
        dice = [dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]

    if graph[x][y] == 0:
        graph[x][y] = dice[5]
    else:
        dice[5] = graph[x][y]
        graph[x][y] = 0

    print(dice[0])



for n in orders:
    nx = x + dir[n][0]
    ny = y + dir[n][1]
    if 0<= nx <N and 0 <= ny < M :
        x, y = nx, ny
        move(x,y,n)



