import sys
from collections import deque
n,k = map(int,sys.stdin.readline().strip().split())
visited = [-1] * 100001

def bsf(v):
    q= deque()
    q.append(v)
    visited[v] = 0

    while(q): 
        cur_v = q.popleft()
        for i in range(3):
            if(i==0):next_v =cur_v +1
            elif(i==1):next_v = cur_v -1
            else:next_v = cur_v*2
            if(0<=next_v <= 100000 and visited[next_v] == -1):
                q.append(next_v)
                visited[next_v]= visited[cur_v]+1
            if(next_v==k):
                print(visited[next_v])
                return 
     

bsf(n)

            
    
    
