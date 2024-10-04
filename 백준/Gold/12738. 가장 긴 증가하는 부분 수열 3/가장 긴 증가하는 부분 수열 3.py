n = int(input())
lis = list(map(int,input().split()))
result = [-float('inf')]

def binary(idx):
  if result[-1]< lis[idx]:
    result.append(lis[idx])
    return
  l, r = 0,len(result)-1
  while(l<=r):
    mid = (l+r)//2
    if result[mid] >=lis[idx]:
      r = mid-1
    else:
      l = mid+1
  result[l] = lis[idx]

for i in range(n):
  binary(i)

print(len(result)-1)
