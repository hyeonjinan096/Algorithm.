import sys

W = int(input())

for i in range(W):
    s = sys.stdin.readline().split()

    for j in range(len(s)):
        if j==len(s)-1:
            print(s[j][::-1])
        else:
            print(s[j][::-1],end=' ')