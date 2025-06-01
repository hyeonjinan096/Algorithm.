N = int(input())
work = []

for _ in range(N):
  t,p = map(int,input().split())
  work.append([t,p])

dp = [0]*(N+1)

for i in range(N):
  t = work[i][0]
  p = work[i][1]
  if(i+t-1 < N):
    for j in range(N,i+t-1,-1):
        dp[j] = max(dp[j],dp[i] + p)

print(dp[N])