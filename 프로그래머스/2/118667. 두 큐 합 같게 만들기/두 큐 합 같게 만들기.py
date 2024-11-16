from collections import deque
def solution(queue1, queue2):
    answer = -1
    q1_sum = sum(queue1)
    mid_sum = (q1_sum + sum(queue2))//2
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    for i in range(300001):
        if q1_sum == mid_sum:
            answer = i
            break
        elif q1_sum < mid_sum:
            tmp = q2.popleft()
            q1.append(tmp)
            q1_sum+=tmp
        else:
            tmp = q1.popleft()
            q2.append(tmp)
            q1_sum-=tmp
    
    return answer