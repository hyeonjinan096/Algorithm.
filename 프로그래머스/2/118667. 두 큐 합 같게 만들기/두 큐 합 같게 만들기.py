from collections import deque

def solution(queue1, queue2):
    #최소 작업 횟수, 없을 경우 -1
    answer = 0
    #합이 같아져야함
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_q1,sum_q2 = sum (q1) , sum(q2)
    S = (sum_q1 + sum_q2)//2
    
    for _ in range(300000):
        if sum_q1 == S:
            return answer
        answer+=1
        if sum_q1 < S:
            tmp = q2.popleft()
            q1.append(tmp)
            sum_q1+=tmp
        else:
            tmp = q1.popleft()
            q2.append(tmp)
            sum_q1-=tmp
    
    return -1