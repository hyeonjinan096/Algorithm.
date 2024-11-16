def solution(n, k):
    answer = 0
    word = ''
    while(n):
        word = str(n%k) + word
        n //=k
        
    def isSosu(x):
        if x<2: return False
        if x == 2: return True
        for i in range(2,int(x**(0.5))+1):
            if x%i == 0:
                return False
        return True
    
    lst = word.split('0')

    for l in lst:
        if l == '':
            continue
        num = int(l)
        if isSosu(num):
            answer+=1
    
    return answer