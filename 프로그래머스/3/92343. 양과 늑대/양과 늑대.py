def solution(info, edges):
    answer = 0
    visited = [0]*len(info)

    def dfs(sheep, wolf):
        nonlocal answer
        
        if sheep <= wolf:
            return
        
        answer = max(sheep, answer)
        for x,y in edges:
            if visited[x] ==1 and visited[y] == 0:
                visited[y] = 1
                if info[y] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[y] = 0
                
    visited[0] = 1        
    dfs(1,0)
    
    return answer