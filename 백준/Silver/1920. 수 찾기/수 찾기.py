import sys

n = int(input())
a = list(map(int,sys.stdin.readline().split()))
m = int(input())
b = list(map(int,sys.stdin.readline().split()))

map = {}
for i in a:
    map[i] = 0

for i in b:
    if(i in map):
        print(1)
    else:
        print(0)
    
