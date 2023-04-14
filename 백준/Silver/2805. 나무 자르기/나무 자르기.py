import sys

n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()

y = 0
sum = 0
s = 0
e = max(arr)
f=0
while(s<=e):
    M = (s+e)//2
    #print("[%d]"%(M))
    sum = 0
    for i in arr:
        if(i>M):
            sum+=(i-M)
    #print("<%d>"%(sum))
    if(sum>=m):
        s=M+1
    else:
        e=M-1
print(e)
    



