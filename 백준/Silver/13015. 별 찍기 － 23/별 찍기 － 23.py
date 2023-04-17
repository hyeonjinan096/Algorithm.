import sys
n = int(sys.stdin.readline())

for i in range(n*2-1):
    if(i == 0 or i == n*2-2):
        print("*"*n+" "*(2*n-3)+"*"*n)
    else:
        if(i>(n-1)):
            i = (2*n-2)-i
        print(" "*(i)+"*"+" "*(n-2)+"*",end ="")
        if((n%2==0 and i ==n-1)or(n%2!=0 and i==n-1)):
            print("",end="")
        else:
            print(" "*(2*n - 3-2*i),end="")
            print("*",end="")
        print(" "*(n-2)+"*")

    



        
