def solution(n):
    answer = 0
    left, right, s = 1, 1, 1
    
    while left <= n:
        if s == n:
            answer += 1
            s -= left
            left += 1
        elif s < n:
            right += 1
            s += right
        else:  # s > n
            s -= left
            left += 1
            
    return answer
