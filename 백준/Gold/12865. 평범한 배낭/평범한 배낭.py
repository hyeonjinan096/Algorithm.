N, K = map(int, input().split())

lst = []
for _ in range(N):
    w,v = map(int, input().split())
    lst.append([w,v])

dp = [0]*(K+1)
for i in range(N):
    w = lst[i][0]
    v = lst[i][1]
    for j in range(K,w-1,-1):
        dp[j] = max(dp[j],dp[j-w] + v)

print(dp[K])