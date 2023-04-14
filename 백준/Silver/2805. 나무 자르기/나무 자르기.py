import sys

n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()

sum = 0
s,e =0,max(arr)

while(s<=e):
    M = (s+e)//2
    sum = 0
    for i in arr:
        if(i>M):
            sum+=(i-M)
    if(sum>=m):
        s=M+1
    else:
        e=M-1
print(e)
    



