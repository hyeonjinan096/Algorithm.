N = int(input())
values = list(map(int,input().split()))

dp = [[0]*21 for _ in range(N-1)]
dp[0][values[0]] = 1

#vlues 돌면서 만들 수 있는 거 check
for i in range(1,N-1):
  for j in range(21):
    if dp[i-1][j] > 0:
      if 0<=j+values[i]<21:
        dp[i][j+values[i]]+=dp[i-1][j]
      if 0<=j-values[i]<21:
        dp[i][j-values[i]]+=dp[i-1][j]

print(dp[-1][values[-1]])


