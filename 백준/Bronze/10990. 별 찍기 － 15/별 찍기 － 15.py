import sys

n = int(sys.stdin.readline())

for i in range(n):
    print(" "*(n-i-1),end="")
    print("*",end="")
    if(i!=0):
        print(" "*(i*2-1),end="")
        print("*")
    else:
        print()


