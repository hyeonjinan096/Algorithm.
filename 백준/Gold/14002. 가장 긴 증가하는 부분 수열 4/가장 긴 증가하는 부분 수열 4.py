import sys
from bisect import bisect_left

n = int(input())
nums = list(map(int,input().split()))

res = []
idx_res = []

for num in nums:
  idx=bisect_left(res, num)
  if idx == len(res):
    res.append(num)
    idx_res.append(idx)
    continue
  res[idx] = num
  idx_res.append(idx) 

answer = []
order = len(res)-1
for i in range(n-1,-1,-1):
  if idx_res[i] == order:
    answer.append(nums[i])
    order-=1

print(len(answer))
print(*answer[::-1])