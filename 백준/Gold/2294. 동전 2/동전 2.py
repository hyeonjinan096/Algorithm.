n,k = map(int,input().split())
lst = [int(input()) for _ in range(n)]

dp = [float("inf")] * (k+1)
dp[0] = 0

for l in lst:
    for i in range(l,k+1):
        dp[i] = min(dp[i], dp[i-l] +1)

if dp[k] == float("inf"):
    print(-1)
else:
  print(dp[k])