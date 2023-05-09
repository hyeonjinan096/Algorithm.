import sys

n = int(sys.stdin.readline())
N=2*n-1
for i in range(n):
    print(" "*i,end="")
    print("*"*(N-(i*2)))

for i in reversed(range(n-1)):
    print(" "*i,end="")
    print("*"*(N-2*i))