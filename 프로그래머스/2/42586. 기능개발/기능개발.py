import math

def solution(progresses, speeds):
    answer = []
    task = []
    
    for i,v in enumerate(progresses):
        task.append(math.ceil((100 - v)/speeds[i]))  

    tmp = task[0]
    day = 0
    for x in task:
        if tmp >= x:
            day+=1
        else:
            answer.append(day)
            tmp = x
            day = 1
    answer.append(day)
    
    return answer