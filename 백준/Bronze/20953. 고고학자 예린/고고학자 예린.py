import sys
n=int(sys.stdin.readline())
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    print((a+b)*(a+b)*(a+b-1)//2)