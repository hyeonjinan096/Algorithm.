import sys

N = int(sys.stdin.readline())

dp = [0 for i in range(N+1)]

if(N > 1) :
    dp[1] = 3
    dp[2] = 7
    for i in range(3,N+1):
        dp[i] = (dp[i-1]*2 + dp[i-2])%9901
elif(N == 1):
    dp[N]=3
    
print(dp[N])