#12:13 18
#시간초과
import sys

N,M = map(int,sys.stdin.readline().split())
values = list(map(int,sys.stdin.readline().split()))

dp = [0]*200001

end = 0
answer = 0
for i in range(N):
  if i > 0:
    dp[values[i-1]]-=1
  for j in range(end, N):
    end = j
    if dp[values[j]]+1>M:
      break
    dp[values[j]]+=1
    answer = max(answer, j-i+1)

print(answer)
