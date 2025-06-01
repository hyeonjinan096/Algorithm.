N, K = map(int,input().split())

subjects = []

for _ in range(K):
    I,T = map(int,input().split())
    subjects.append([I,T])

#최대 중요도 공부 시간별 - 중요도 
dp = [0] * (N+1)

for  i in range(K):
    important = subjects[i][0]
    time = subjects[i][1]

    for j in range(N, time-1, -1):
        dp[j] = max(dp[j], dp[j - time] + important)

print(dp[N])