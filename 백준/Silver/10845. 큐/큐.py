import sys
from collections import deque

N = int(input())
q = deque()

for i in range(N):
    S = sys.stdin.readline().split()
    s=S[0]
    if(s =="push"):
        q.append(S[1])
    elif s=="pop":
        if(not q):
            print(-1)
        else:
            print(q.popleft())
    elif s=="size":
        print(len(q))
    elif s=="empty":
        if(not q):
            print(1)
        else: print(0)
    elif s=="front":
        if(not q):
            print(-1)
        else:
            print(q[0])
    elif s=="back":
        if not q:
            print(-1)
        else:
            print(q[-1])

    



