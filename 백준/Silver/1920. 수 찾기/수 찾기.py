import sys

n = int(input())
a = list(map(int,sys.stdin.readline().split()))
m = int(input())
b = list(map(int,sys.stdin.readline().split()))

a.sort()


for i in b:
    s = 0
    e = n-1
    f = 0
    while(s<=e):
        M = (s+e)//2
        if(a[M]<i):
            s = M+1
        elif(a[M]>i):
            e = M-1
        else:
            f = 1
            print(1)
            break
    if(f == 0):
        print(0)