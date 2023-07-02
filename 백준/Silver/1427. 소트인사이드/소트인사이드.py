import sys

s = list(sys.stdin.readline().strip())

s.sort(reverse=True)

for i in s:
    print(i,end="")