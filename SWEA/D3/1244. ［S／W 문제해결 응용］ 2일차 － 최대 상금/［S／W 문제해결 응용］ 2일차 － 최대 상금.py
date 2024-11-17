T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    value,k = input().split()
    value = list(value)
    k = int(k)
    l = len(value)
    dp = [[] for _ in range(11)]

    answer = 0
    def dfs(cnt):
      global answer
      if cnt > k:
        return
      if cnt == k:
        num=int(''.join(value))
        answer= max(answer, num)
        return 
      
      for i in range(l):
        for j in range(i+1,l):
          value[i],value[j] = value[j],value[i]
          num = int(''.join(value))
          if num not in dp[cnt]:
            dp[cnt].append(num)
            dfs(cnt+1)
          value[i],value[j] = value[j],value[i]
    
    dfs(0)

    print(f'#{test_case} {answer}')