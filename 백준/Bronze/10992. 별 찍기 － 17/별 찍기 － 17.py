import sys
m =int(sys.stdin.readline())
k=1

for i in range(1,m+1):
    print(" "*(m-i),end="")
    if( i==1):
        print("*")
    elif(i==m):
        print("*"*(k+2))
    else:
        print("*"+" "*k+"*")
        k+=2


