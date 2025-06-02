N,K = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(K)]


dp = [0] * 10001
for i in range(K):
    important = lst[i][0]
    time = lst[i][1]
    for j in range(N,time-1,-1):
        dp[j] = max(dp[j],dp[j -time] + important)

print(dp[N])