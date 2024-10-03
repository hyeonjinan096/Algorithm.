from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sumq1 = sum(queue1)
    sumq2 = sum(queue2)
    
    for i in range(300000):
        if sumq1 == sumq2:
            return answer
        elif sumq1 > sumq2:
            tmp = q1.popleft()
            q2.append(tmp)
            sumq2+=tmp
            sumq1-=tmp
        else:
            tmp = q2.popleft()
            q1.append(tmp)
            sumq1+=tmp
            sumq2-=tmp
        answer+=1

    return -1