import sys
n = int(input())
num = list(map(int, sys.stdin.readline().split()))

dr= {}
for v in num:
    dr[v] = 0
numl = num[:]
num.sort()#오름차순 정렬

j = -1
k = -1
for i in num:
    if(k!=i):
        j+=1
    dr[i] = j
    k = i

for i in numl:
    print(dr[i], end=" ")