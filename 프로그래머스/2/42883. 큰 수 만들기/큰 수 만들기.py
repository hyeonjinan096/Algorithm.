# from collections import deque

def solution(number, k):
    answer = []
    
    for num in number:
        while(len(answer) > 0 and k> 0 and answer[-1] < num):
            answer.pop()
            k-=1
        answer.append(num)
    
    while(k>0):
        answer.pop()
        k-=1
    
    
    return ''.join(answer)

