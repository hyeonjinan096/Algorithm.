from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    q1_sum=sum(queue1)
    q2_sum = sum(queue2)
    S = (q1_sum + q2_sum) //2
    
    
    for i in range(300000):
        if q1_sum == S:
            return i
    
        if q1_sum < S:
            x = queue2.popleft()
            queue1.append(x)
            q1_sum+=x
        else:
            x= queue1.popleft()
            queue2.append(x)
            q1_sum-=x
            
    return -1

