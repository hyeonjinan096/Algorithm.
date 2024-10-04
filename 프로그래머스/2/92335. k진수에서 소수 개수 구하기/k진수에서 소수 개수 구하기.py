def solution(n, k):
    #소수 갯수
    answer = 0
    
    #k진수로 변환하기 
    world = ""
    while(n):
        world = str(n%k) + world
        n //= k
    
    lst = world.split('0')
   
    for l in lst:
        if len (l) == 0:
            continue    
        num = int(l)
        #0,1제외
        if num < 2:
            continue
        sosu = True
        for j in range(2, int(num**0.5)+1):
            if num % j == 0:
                sosu = False
        if sosu:
            answer+=1
    
    return answer