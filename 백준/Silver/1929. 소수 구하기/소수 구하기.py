import sys
n,m =map(int, sys.stdin.readline().split())

for i in range(n,m+1):
    if(i==1):
        pass
    else:
        p=0
        for j in range(2,int(i**0.5)+1):
            if(i%j==0):
                p=1
                break
        if(p==0):
            print(i)
