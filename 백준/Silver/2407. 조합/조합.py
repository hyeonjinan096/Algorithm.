n,m = map(int,input().split())
a = 1
b = 1
for i in range(n,n-m,-1):
    a*=i
for i in range(m,0,-1):
    b*=i
print(a//b)