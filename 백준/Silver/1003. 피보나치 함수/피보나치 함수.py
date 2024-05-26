T = int(input())

for i in range(T):
    n = int(input())
    dp = [0]*(n+2)
    dp[0] = [1, 0]
    dp[1] = [0, 1]
    for j in range(2, n + 1):
        dp[j] = [dp[j - 1][0] + dp[j - 2][0], dp[j - 1][1] + dp[j - 2][1]]
    print(*dp[n])
