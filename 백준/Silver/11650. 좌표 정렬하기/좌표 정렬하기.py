import sys
n = int(sys.stdin.readline())

k=[[]*2 for _ in range(n)]

for i in range(n):
    k[i] = list(map(int,sys.stdin.readline().split()))
k.sort()

for i in range(n):
    print("%d %d" %(k[i][0],k[i][1]))