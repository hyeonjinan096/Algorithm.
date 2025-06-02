from heapq import heappop, heappush, heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    cnt = 0
    while(len(scoville)>1):
        x = heappop(scoville)
        if x >= K:
            break
        y = heappop(scoville)
        cnt += 1
        heappush(scoville, x + (y*2))
    
    if heappop(scoville) < K:
        return -1
    else:
        return cnt
    