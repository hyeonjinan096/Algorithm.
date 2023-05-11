import sys
from collections import deque

n,b = map(int,sys.stdin.readline().split())
q= deque()
q.append([n,1])

f=0
while(q):
    k=q[0]
    if(k[0]==b):
        print(k[1])
        f=1
        break
    else:
        q.popleft()
        if(k[0]*2<=b):
            q.append([k[0]*2,k[1]+1])
        if(k[0]*10+1<=b):
            q.append([k[0]*10+1,k[1]+1])
if(f==0):
    print(-1)


