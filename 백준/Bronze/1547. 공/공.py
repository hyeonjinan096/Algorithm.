import sys
M = int(input())
a = [0,1,2,3]

for _ in range(M):
    x, y = map(int, input().split())
    a[x], a[y] = a[y], a[x]

print(a.index(1))