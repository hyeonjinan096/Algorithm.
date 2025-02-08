import sys

N,C = map(int,sys.stdin.readline().split())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))
lst.sort()

def check(m):
    cnt,tmp = 0, 0
    for i in range(N):
        if i == 0 or lst[i] - lst[tmp] >= m:
            tmp = i
            cnt+=1
    return cnt

start, end = 0, lst[-1] - lst[0] + 1
answer = 0
while(start<end):
    m = (start + end)//2
    if check(m) < C:
        end = m
    else:
        start = m+1
        answer = m

print(answer)