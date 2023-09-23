import sys
a, b, c, d = map(int, sys.stdin.readline().split())
i = 0
for i in range(a):
    A = input()
    for k in range(c):
        for j in range(b):
            res = A[j] * d
            print(res, end='')
        print()