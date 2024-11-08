T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    values = [list(map(int,input().split(' '))) for _ in range(N)]
    visited = [0]*N
    
    answer = 0

    def dfs(n,score,cal):
        global answer
        if cal>M:
            return
        answer = max(score, answer)
        
        for i in range(n,N):
            if not visited[i]:
                visited[i] = 1
                dfs(i,score+values[i][0], cal+values[i][1])
                visited[i] = 0
        

    for n in range(N):
        visited[n] = 1
        dfs(n,values[n][0],values[n][1])
        visited[n] = 0
    
    print(f'#{test_case} {answer}')
