import sys

N,M = map(int, sys.stdin.readline().strip().split())
x,y,z = map(int, sys.stdin.readline().strip().split())
g =[]

for i in range(N):
    g.append(list(map(int,sys.stdin.readline().strip().split())))


count = 0
dx = [-1,0,1,0]#0,1,2,3
dy = [0,1,0,-1]

def clean(x,y,z):
    global count
    
    #청소 
    if(g[x][y]==0):
        g[x][y] = 2
        count +=1
    
    #탐색
    Z= z
    #청소할 방이 있는가
    for i in range(4):
        Z = (Z+3) % 4
        if(g[x+dx[Z]][y+dy[Z]]==0):
            clean(x+dx[Z],y+dy[Z],Z)
            return
    #후진이 가능한가
    if(g[x-dx[z]][y-dy[z]]!=1):
        clean(x-dx[z],y-dy[z],z)
        return 
    else:
        return count


clean(x,y,z)
print(count)


    
    

