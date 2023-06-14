def solution(s):
    answer = []
    d = {a:-1 for a in s}
    
    for i in range(len(s)):
        if(d[s[i]]==-1):
            answer.append(-1)
        else:
            print(d[s[i]])
            answer.append(i-d[s[i]])
        d[s[i]]=i
 
    return answer