import sys
a, b = map(int, sys.stdin.readline().split())

count = 0

def dfs(N):
    global count
    if(a<= N <=b):
        count+=1
    for i in [4,7]:
        current_N = N*10 + i
        if(current_N <=b):
            dfs(current_N)
            

dfs(4)
dfs(7)

print(count)