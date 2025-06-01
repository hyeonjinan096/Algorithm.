#한개, 두개
#연속 세개 안됨
#최대 총점

N = int(input())
lst = [int(input()) for _ in range(N)]

dp = [0]*N
dp[0] = lst[0]

for i in range(1,N):
    if i == 1:
       dp[1] = lst[1] + lst[0]
    elif i == 2:
      dp[i] = max(lst[i-2], lst[i-1]) + lst[i]
    else:    
      dp[i] = max(dp[i-2] + lst[i], dp[i-3] + lst[i-1] + lst[i])

print(dp[N-1])