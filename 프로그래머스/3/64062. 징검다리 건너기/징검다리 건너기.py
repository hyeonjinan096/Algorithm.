def solution(stones, k):
    answer = 0
    left = 1
    right = 200000000
    while left <= right:
        mid = (left + right)//2
        cnt = 0 
        for i in stones:
            tmp = i-mid
            if tmp <=0:
                cnt+=1
            else:
                cnt = 0 
            if cnt >= k:
                break
        if cnt >= k:
            right = mid-1
        else: 
            left = mid + 1
    
    return left