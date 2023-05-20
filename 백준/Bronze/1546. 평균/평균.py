import sys

n = int(sys.stdin.readline())
s = list(map(int,sys.stdin.readline().strip().split()))

M = max(s)
for i in range(n):
        s[i]=s[i]/M*100

print(sum(s)/n)