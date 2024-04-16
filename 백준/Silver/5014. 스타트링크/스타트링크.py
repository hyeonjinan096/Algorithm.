import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())
count = [0 for _ in range(F+1)]

def bfs():
    q = deque()
    q. append(S)
    count[S] = 1
    while q:
        cur = q.popleft()
        if cur == G:
            print(count[cur]-1)
            break
        for next in (cur+U, cur-D):
            if 0<next<F+1 and count[next] == 0:
                count[next]=count[cur]+1
                q.append(next)

    if count[G] == 0:
        print("use the stairs") 

bfs()

