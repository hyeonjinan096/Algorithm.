import sys
n = int(sys.stdin.readline())
a={}
for i in range(n):
    s,a[s]= list(sys.stdin.readline().split())

a=dict(sorted(a.items(),reverse=True))

for i in a:
    if(a[i]!="leave"):
        print(i)
    



