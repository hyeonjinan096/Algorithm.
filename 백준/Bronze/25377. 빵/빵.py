from sys import stdin
n = int(stdin.readline().strip())
k = 1001
for i in range(n):
    a, b = map(int, stdin.readline().split())
    if b>=a:
        if b<k:
            k = b
if k != 1001:
    print(k)
else:
    print(-1)
    print(k)