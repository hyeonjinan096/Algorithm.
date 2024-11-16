def solution(triangle):
    answer = 0
    for i in range(1,len(triangle)):
        for j in range(0,len(triangle[i])):
            arr = []
            if 0<=i-1 and 0<=j-1:
                arr.append(triangle[i-1][j-1])
            if 0<=i-1 and 0<=j<=i-1:
                arr.append(triangle[i-1][j])
            triangle[i][j] += max(arr)
    return max(triangle[-1])

