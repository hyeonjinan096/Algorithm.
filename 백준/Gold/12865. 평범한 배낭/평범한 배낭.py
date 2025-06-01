N, K = map(int,input().split())

thing = []


for _ in range(N):
  w,v = map(int,input().split())
  thing.append([w,v])

dp = [0 for _ in range(K+1)]
dp[0] = 0

for i in range(N):
  weight = thing[i][0]
  value = thing[i][1]
  for j in range(K,weight-1,-1):
    dp[j] = max(dp[j],dp[j-weight] + value)

print(dp[K])