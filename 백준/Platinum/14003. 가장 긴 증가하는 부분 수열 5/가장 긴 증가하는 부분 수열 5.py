from bisect import bisect_left
N = int(input())
nums = list(map(int,input().split()))
result = []
idx_value = []

for num in nums:
  idx = bisect_left(result,num)
  if idx == len(result):
    result.append(num)
  else:
    result[idx] = num
  idx_value.append(idx+1)

order = len(result)
answer = []
for i in range(N-1,-1,-1):
  if idx_value[i] == order:
    answer.append(nums[i])
    order-=1

print(len(result))
print(*answer[::-1])