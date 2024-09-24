import sys

N = int(input())
value = sys.stdin.readline().split()
m = int(input())
stu = [list(map(int, sys.stdin.readline().split())) for _ in range(m) ]

def switch(n):
  if n =='1':
    return '0'
  else: 
    return '1'

for s,n in stu:
  if s==1:
    for i in range(n-1,N,n):
      value[i] = switch(value[i])

  else:
    n-=1
    value[n] = switch(value[n])
    x,y = n-1, n+1
    while(0<=x<N and 0<=y<N):
      if value[x] == value[y]:
        value[x] = switch(value[x])
        value[y] = switch(value[y])
        x-=1
        y+=1
      else:
        break


for i in range(N):
  if((i+1)%20 ==0 ):
    print(value[i],end="\n")
  else: print(value[i], end = " ")
