import sys

N = int(sys.stdin.readline())
n = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
m = list(map(int,sys.stdin.readline().split()))

d = {}
for i in range(N):
    d[n[i]]=1
for i in range(M):
    if(m[i] in d):
        print("1 ",end="")
    else:
        print("0 ",end="")


