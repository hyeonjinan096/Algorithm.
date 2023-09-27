import sys

N = int(sys.stdin.readline())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))

num.sort(reverse=True)


for i in num:
    print(i)