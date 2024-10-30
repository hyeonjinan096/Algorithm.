#3:31
import sys

N = int(sys.stdin.readline())
values = list(map(int,sys.stdin.readline().split()))
dp = [[0]*21 for _ in range(N-1)]
dp[0][values[0]] = 1

for i in range(1,N-1):
  for j in range(21):
    if dp[i-1][j] > 0:
      if 0<=j + values[i]<=20:
        dp[i][j+values[i]]+=dp[i-1][j]
      if 0<=j - values[i]<=20:
        dp[i][j-values[i]]+=dp[i-1][j]

print(dp[-1][values[-1]])