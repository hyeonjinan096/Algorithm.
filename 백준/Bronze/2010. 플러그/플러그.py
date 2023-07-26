import sys

n = int(sys.stdin.readline())
sum = 1
for i in range(n):
    y = int(sys.stdin.readline())
    sum=sum +y

print(sum-n)