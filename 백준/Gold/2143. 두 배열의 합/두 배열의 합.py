import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

T = int(input())
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

a_sum = []
for i in range(n):
    for j in range(i,n):
        a_sum.append(sum(a[i:j+1]))

b_sum = []
for i in range(m):
    for j in range(i,m):
        b_sum.append(sum(b[i:j+1]))

a_sum.sort()
b_sum.sort()

answer= 0
for a in a_sum:
    answer += bisect_right(b_sum, T-a) - bisect_left(b_sum, T-a)

print(answer)