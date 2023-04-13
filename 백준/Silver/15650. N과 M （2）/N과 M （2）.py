import sys
n, m = map(int,sys.stdin.readline().split())
num = [0 for i in range(m)]

def dfs(index):
    if(index ==m):
        print(" ".join(map(str,num)))
        return
    for i in range(1, n+1):
        if(i not in num)and(i>max(num)):
            num[index] = i
            dfs(index+1)
            num[index] = 0
dfs(0)
