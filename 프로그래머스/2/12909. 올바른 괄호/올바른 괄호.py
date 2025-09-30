from collections import deque

def solution(s):
    q = deque([])
    
    for i in s:
        if i == '(':
            q.append(i)
        else:
            if q and q[0] == '(':
                q.popleft()
            else:
                return False
    if len(q) > 0:
        return False

    return True