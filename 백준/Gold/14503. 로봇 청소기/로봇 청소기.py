import sys

n,m = map(int,sys.stdin.readline().strip().split())
x,y,z = map(int,sys.stdin.readline().strip().split())
g =[]
for _ in range(n):
    g.append(list(map(int,sys.stdin.readline().strip().split())))
visited=[[False]*m for _ in range(n)]



def check(x,y):
    #print("%d,%d"%(x,y))
    if g[x][y] == 1:
        return 1  #벽일때
    if visited[x][y] :
        return 2  #이미 청소했을 때
    return 0





def clean(x,y,z,count): #자리+방향
    if(check(x,y)==0):
        count+=1

    #print("(%d,%d,%d) count = %d,"%(x,y,z,count))

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    visited[x][y] = True
    flag = 0
    if(flag==0):
        Z = z
        for _ in range(4):
            Z -=1   #시계방향을 돌리기
            if(Z<0): Z =3
            if(check(x+dx[Z],y+dy[Z])==0):
                #print("%d->%d 청소가능"%(z,Z))
                clean(x+dx[Z],y+dy[Z],Z,count)
                return 
                #flag = 1
                #break
    if(flag==0):
        #print("back")
        if(z == 0):b=2
        elif(z==2):b=0
        elif(z==3):b=1
        elif(z==1):b=3 #후진하기 b = 후진방향
        if check(x-dx[z],y-dy[z])!=1: # 벽이 아니면 후진
            #print("%d->%d 후진"%(z,b))
            clean(x+dx[b],y+dy[b],z,count)
            return 
        else: #벽이면 중지
            #print("멈춤!")
            print(count)
            return 
        
    
        




clean(x,y,z,0)




