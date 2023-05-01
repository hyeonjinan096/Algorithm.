import sys
n,m = map(int, sys.stdin.readline().split())
s = list(map(int,sys.stdin.readline().split()))
s += list(map(int,sys.stdin.readline().split()))
#s=list(set(s))
s.sort()
print(*s)