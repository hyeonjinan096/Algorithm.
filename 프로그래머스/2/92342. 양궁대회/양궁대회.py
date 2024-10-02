def solution(n, info):
    answer = [-1]
    Max = 0
    lion = [0]*11
    
    def score():
        L, A = 0,0
        for i in range(11):
            if lion[i] > info[i]:
                L +=(10-i)
            elif lion[i] <= info[i] and info[i]!=0:
                A+=(10-i)
        return L>A, abs(L-A)
    
    def dfs(idx,n):
        nonlocal answer,Max
        
        if n == 0 or idx == 10:
            lionIsWinner, num = score()
            if lionIsWinner:
                if n>0 : 
                    lion[-1] = n
                if Max < num: 
                    Max = num
                    answer = lion[:]
                elif Max == num:
                    for i in range(10,-1,-1):
                        if answer[i] < lion[i]:
                            answer = lion[:]
                            break
                        elif answer[i] > lion[i]:
                            break
                lion[-1] = 0
            return
        #이기는 경우
        if n-(info[idx]+1)>=0:
            lion[idx] = info[idx]+1
            dfs(idx+1,n-(info[idx]+1))
            lion[idx] = 0
        dfs(idx+1,n)     
    
    dfs(0,n)
    return answer