def solution(info, edges):
    answer = 0
    graph = [[] for _ in range(len(info))]
    for x,y in edges:
        graph[x].append(y)
    
    def dfs(x, sheep, wolf, possible):
        nonlocal answer
        
        if info[x] == 0:
            sheep+=1
            answer = max(answer,sheep)
        else:
            wolf+=1
            
        if sheep <= wolf:
            return
        possible.extend(graph[x])
 
        for p in possible:
            dfs(p, sheep, wolf, [i for i in possible if i !=p])
    
    dfs(0,0,0,[])
    
    return answer