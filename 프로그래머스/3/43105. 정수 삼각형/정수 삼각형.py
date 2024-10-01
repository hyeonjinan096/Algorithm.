def solution(triangle):
    answer = 0
    
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            tmp = triangle[i][j] 
            if 0<=j-1<len(triangle[i-1]):
                triangle[i][j] = max(triangle[i][j],tmp +triangle[i-1][j-1])
            if 0<=j<len(triangle[i-1]):
                triangle[i][j] = max(triangle[i][j],tmp +triangle[i-1][j])
                    
    
    return max(triangle[-1])


                    
    