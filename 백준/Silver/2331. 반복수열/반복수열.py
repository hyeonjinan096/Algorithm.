import sys
a, p = map(int,sys.stdin.readline().strip().split())
  
count =-1
visited ={}
def dfs(cur_v,count):
    count+=1
    sum =0
    visited[cur_v]=count
    while(cur_v!=0):
        n=1
        N = cur_v%10
        cur_v = cur_v //10
        for _ in range(p):
            n *= N
        sum += n 
    if(sum not in visited):
        dfs(sum,count)
    else:
        print(visited[sum]-1)
        return 
    
dfs(a,0)