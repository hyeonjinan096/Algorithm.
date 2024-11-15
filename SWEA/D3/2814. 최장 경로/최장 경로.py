T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    graph = {}
    for _ in range(M):
        x,y = map(int,input().split())
        if x not in graph:
            graph[x] = []
        if y not in graph:
            graph[y] = []
        
        graph[x].append(y)
        graph[y].append(x)
    
    #모든 곳 돌면서 가장 긴거 찾기 
    #dfs?
    visited = [0]*(N+1)
    answer = 0

    def dfs(x,cnt):
        global answer
        answer = max(answer, cnt)
        if x not in graph:
            return
        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                dfs(i,cnt+1)
                visited[i] = 0
        
    
    for i in range(1,N+1):
        visited[i] = 1
        dfs(i,1)
        visited[i] = 0

    print(f'#{test_case} {answer}')