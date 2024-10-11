import sys
N = int(input())
values = list(map(int,sys.stdin.readline().split()))
M = int(input())

l, r = 0,max(values)

while(l<=r):
  mid = (l+r)//2
  result = 0
  for value in values:
    if value <= mid:
      result+=value
    else:
      result+=mid
  if result>M:
    r = mid-1
  else:
    l = mid+1

print(r)
