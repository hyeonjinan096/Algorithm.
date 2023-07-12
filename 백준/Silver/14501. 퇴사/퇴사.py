
import sys


N = int(sys.stdin.readline())
li = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]

s =[0]
for i in range(N-1,-1,-1):
    S = li[i][0]
    M = li[i][1]
    MAX = M
    if(i+S-1)>=N:
        li[i][1] = -1
        continue
    for j in range(i+S,N):
        if(li[j][1] != -1 ):
            MAX = max(MAX, M + li[j][1])
            
    li[i][1] = MAX
    s.append(li[i][1])


print(max(s))