from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_q1 = sum(queue1)
    same = (sum_q1 + sum(queue2))//2
    
    for i in range(300000):
        if sum_q1 == same:
            return answer
        answer+=1
        if sum_q1 < same:
            new = q2.popleft()
            q1.append(new)
            sum_q1+=new
        else:
            new = q1.popleft()
            q2.append(new)
            sum_q1-=new
            
    return -1