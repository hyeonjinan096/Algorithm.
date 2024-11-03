import sys

N,K = map(int,sys.stdin.readline().split(' '))
dp = [0]*200001
values = list(map(int,sys.stdin.readline().split(' ')))
last_check = 0
answer = 0
len = 0

for i in range(0,N):
  if i-1 > -1:
    dp[values[i-1]]-=1
    len-=1

  for j in range(last_check,N):
    last_check = j
    if dp[values[j]]+1 > K:
      break
    dp[values[j]]+=1
    len+=1
  answer = max(len, answer)

print(answer)




