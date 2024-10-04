import sys
from bisect import bisect_left

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))

dp = []
dp_idx = []

for num in numbers:
    idx = bisect_left(dp,num)
    if idx == len(dp):
        dp_idx.append(len(dp))
        dp.append(num)
        
        continue
    dp[idx] = min(num, dp[idx])
    dp_idx.append(idx)

idx = len(dp) - 1
idx_num = 1000000001

result = []

for i in range(n - 1, -1, -1):
    if idx == dp_idx[i] and numbers[i] < idx_num:
        result.append(numbers[i])
        idx -= 1
        idx_num = numbers[i]


print(len(dp))
print(*result[::-1])