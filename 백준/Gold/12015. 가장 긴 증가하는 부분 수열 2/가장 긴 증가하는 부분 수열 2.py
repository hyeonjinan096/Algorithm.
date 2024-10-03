
n = int(input())
cases = list(map(int,input().split()))
lis = [0]

for case in cases:
  if lis[-1]<case:
    lis.append(case)
  else:
    left = 0
    right = len(lis)

    while left<=right:
      mid = (left+right)//2
      if lis[mid]>=case:
        right = mid -1
      else:
        left = mid+1

    lis[left] = case

print(len(lis)-1)

