import sys

n = int(sys.stdin.readline())

for i in range(1,10):
    print(n,end=" * ")
    print(i,end=" = ")
    print(n*i)
    