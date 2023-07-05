import sys
from collections import deque

x = int(sys.stdin.readline().strip())

def fun(start_x):
    q= deque()
    q.append((0,start_x))
    while(q):
        C, cur_x =q.popleft()
        if(cur_x==1):
            return C
        elif(cur_x!=0):
            if(cur_x % 3 == 0): q.append((C+1,cur_x//3))
            if(cur_x % 2 == 0): q.append((C+1,cur_x//2))
            q.append((C+1,cur_x-1))

print(fun(x))

