import sys

N = int(input())
distance = list(map(int,input().split()))
fuel_price = list(map(int,input().split()))

#dp사용 -> O(N)임 -> 시간 초과
#dp를 사용하지 않고 왼쪽부터 순차적으로 하는게 가장 적합
# dp =[float('inf')]*(N-1)

# for i in range(N-2,-1,-1):
#   for j in range(N-2,i-1,-1):
#     dp[j] = min(dp[j],fuel_price[i])

# answer = 0
# for i in range(N-1):
#   answer += dp[i]*distance[i]
# print(answer)

min_price = fuel_price[0]
answer = 0

for i in range(N-1):
  if fuel_price[i] < min_price:
    min_price = fuel_price[i]
  answer += min_price * distance[i]

print(answer)