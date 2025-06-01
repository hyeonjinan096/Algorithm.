from collections import deque

N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]
board[0][0] = 1

for _ in range(K):
    x,y = map(int,input().split())
    board[x-1][y-1] = -1 #apple

L = int(input())
info = {}
for _ in range(L):
    a,b = input().split()
    info[int(a)] = b

dx = [0,1,0,-1]
dy = [1,0,-1,0]
dir = 0
x = 0
y = 0
snake = deque([[0,0]])

time = 0
while(1):
    if time in info.keys():
        if info[time] == "D":
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4

    time += 1

    x = x + dx[dir]
    y = y + dy[dir]

    if x < 0 or x >=N or y <0 or y>=N or board[x][y] == 1:
        break
        
    if board[x][y] == -1:
        snake.append([x,y])
        board[x][y] = 1        
    else:
        tail_x, tail_y=snake.popleft()
        board[tail_x][tail_y] = 0
        snake.append([x,y])
        board[x][y] = 1
        

print(time)
