import copy
def solution(triangle):
    answer = copy.deepcopy(triangle)
    for x in range(len(triangle)-1):
        for y in range(len(triangle[x])): 
            if triangle[x+1][y] + answer[x][y] > answer[x+1][y]:
                answer[x+1][y] =  triangle[x+1][y] + answer[x][y]
            
            if triangle[x+1][y+1] + answer[x][y] > answer[x+1][y+1]:
                answer[x+1][y+1] =  triangle[x+1][y+1] + answer[x][y]
            
        
    
    return max(answer[-1])