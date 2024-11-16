def solution(info, edges):
    answer = 0
    l = len(info)
    visited = [0]*l
    
    def dfs(sheep, wolf):
        nonlocal answer
        
        if sheep <=wolf:
            return
        answer = max(answer,sheep)
        for i,j in edges:
            if visited[i] and not visited[j]:
                visited[j] = 1
                if info[j] == 0:
                    dfs(sheep+1,wolf)
                else:
                    dfs(sheep,wolf+1)
                visited[j] = 0
                
    visited[0] = 1
    dfs(1,0)
    return answer