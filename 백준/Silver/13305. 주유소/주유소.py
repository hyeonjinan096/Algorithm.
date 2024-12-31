import sys

N = int(input())
distance = list(map(int,input().split()))
fuel_price = list(map(int,input().split()))
dp =[float('inf')]*(N-1)

for i in range(N-2,-1,-1):
  for j in range(N-2,i-1,-1):
    dp[j] = min(dp[j],fuel_price[i])

answer = 0
for i in range(N-1):
  answer += dp[i]*distance[i]
print(answer)
