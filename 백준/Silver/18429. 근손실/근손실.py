import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
table = list(map(int, sys.stdin.readline().split()))
visited = [0] * N
result = 0

def find(x,n):
    global result
    if x < 500:
        return
    if n == N :
        result += 1
        return 
    x -= K

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            find(x+table[i], n+1)
            visited[i] = 0

find(500, 0)
print(result)


