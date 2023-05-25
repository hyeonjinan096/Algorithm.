import sys
from collections import deque
n, k = map(int,sys.stdin.readline().strip().split())

def bfs():
    q = deque()             
    q.append(n)           
    while  q:
        v = q.popleft()     
        if v == k:
            print(visited[v])
            break
        for nv in (v - 1, v + 1, v * 2):    
            if 0 <= nv <= MAX and not visited[nv]:
                visited[nv] = visited[v] + 1
                q.append(nv)    

MAX = 10 ** 5               # 시간초과 방지
visited = [0] * (MAX + 1)      # 이동하는 시간 count

bfs()