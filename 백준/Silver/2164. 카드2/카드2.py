import sys
m =int(sys.stdin.readline())

from collections import deque
q= deque()
for i in range(1,m+1):
    q.append(i)
f=1
while(len(q)!=1):
    if(f==1):
       q.popleft() 
       f=2
    elif(f==2):
       q.append(q.popleft())
       f=1

print(q.popleft())


