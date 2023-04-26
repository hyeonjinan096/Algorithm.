import sys

n = int(sys.stdin.readline())
s = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
s2 = list(map(int,sys.stdin.readline().split()))

map = {}
for i in s:
    if(i in map):
        map[i] +=1
    else:
        map[i]=1
for i in s2:
    if(i in map):
        print("%d "%(map[i]),end="")
    else:
        print("0 ",end="")