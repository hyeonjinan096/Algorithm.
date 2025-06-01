import sys
C,N = map(int,input().split())
city = [list(map(int,input().split())) for _  in range(N)]

MAX = 100 * 100 + 1
dp = [float('inf')] * MAX
dp[0] = 0

for cost, customer in city:
  for i in range(customer, C+101):
    dp[i] = min(dp[i], dp[i-customer] + cost)

print(min(dp[C:]))