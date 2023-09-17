import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
sum = 0

x.sort()
dp = [0] * (n + 1)

for i in range(1, n):
    dp[i] = dp[i - 1] + (x[i] - x[i - 1]) * i
    sum += dp[i]
print(sum * 2)