def solution(stones, k):
    answer = 0
    start = 1
    end = 200000000
    
    while(start<=end):
        mid = (start + end)//2
        flag = 0
        cnt = 0
        for stone in stones:
            if stone-mid <=0:
                cnt +=1
                if cnt >= k:
                    flag = 1
                    break
            else:
                cnt = 0
        if flag:
            end = mid-1
        else:
            start = mid+1
    
    return start