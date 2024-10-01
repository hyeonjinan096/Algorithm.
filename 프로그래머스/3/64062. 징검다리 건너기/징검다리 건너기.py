def solution(stones, k):
    answer = 0
    Max = max(stones)
    s, e = 0,Max
    
    while(s<=e):
        m = (s+e)//2
        cnt = 0
        for j in stones:
            if j-m <= 0:
                cnt+=1
            else:
                cnt =0
            if cnt >= k:
                break
        if cnt >=k:
            e = m-1
        if cnt < k:
            s = m+1
            
                
    return s