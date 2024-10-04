from bisect import bisect_left
N = int(input())
nums = list(map(int,input().split()))
result = []

for num in nums:
  idx = bisect_left(result,num)
  if idx == len(result):
    result.append(num)
  else:
    result[idx] = num

print(len(result))