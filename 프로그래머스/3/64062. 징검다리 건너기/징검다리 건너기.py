def solution(stones, k):
    answer = 0
    
    l, r =0, 200000000
    
    while(l<=r):
        mid = (l+r)//2
        max = 0
        for stone in stones:
            if stone - mid <= 0: 
                max+=1
            else:
                max = 0
            if max >=k:
                r = mid-1
                break
        if max < k:
            l = mid+1
    
    return l