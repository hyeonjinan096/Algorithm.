n = int(input())
lis = list(map(int,input().split()))

dp = [1]*n

for i in range(n):
  for j in range(0,i):
    if lis[j] < lis[i]: dp[i] = max(dp[j]+1,dp[i])

answer = []
order = max(dp)
for i in range(n-1,-1,-1):
  if dp[i] == order:
    answer.append(lis[i])
    order-=1



print(max(dp))
print(*answer[::-1])

