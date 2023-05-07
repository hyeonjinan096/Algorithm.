import sys

n = int(sys.stdin.readline())


def func(x,y,c):
    Y=y
    X=x
    while(x<y-2):
        s[x][y]="*"
        x+=1
    while(y>c):
        s[x][y]="*"
        y-=1
    while(x>c):
        s[x][y]="*"
        x-=1
    while(y<=Y-2):
        
        s[x][y]="*"
        y+=1
    if(y==N):return
    else:
        func(X+2,Y-2,c+2) 


if(n==1):
    print("*",end="")
else:
    s= [[' ']*(4*n-1) for _ in range(4*n-3) ]
    for i in range(4*n-3):
        s[i][0]="*"
        s[i][1]=""
    for i in range(4*n-1):
        s[0][i]="*"
    N=2*n+1

    func(0,4*n-2,2)

    for i in range(4*n-1):
        for j in range(4*n-3):
            print(s[j][i],end="")
        print( )
   

