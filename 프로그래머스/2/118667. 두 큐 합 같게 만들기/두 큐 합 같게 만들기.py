from collections import deque
def solution(queue1, queue2):
    answer = -1
    q1_sum = sum(queue1)
    same = (q1_sum+sum(queue2))//2
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    cnt = 0
    for _ in range(300000):
        if q1_sum == same:
            answer = cnt
            break
        if q1_sum < same:
            new = q2.popleft()
            q1.append(new)
            q1_sum += new
        else:
            new = q1.popleft()
            q2.append(new)
            q1_sum -= new
        cnt+=1
            
    
    return answer