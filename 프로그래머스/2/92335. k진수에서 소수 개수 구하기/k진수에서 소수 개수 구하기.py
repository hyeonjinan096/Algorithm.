import math
def solution(n, k):
    answer = 0
    value = ""
    while(n):
        value = str(n%k) + value
        n //= k
    
    arr = value.split('0')
    print(arr)
    for a in arr:
        if len(a) == 0 or int(a)<2:
            continue
        v = int(a)
        print(v)
        sosu = True
        for i in range(2,int(v**0.5)+1):
            if v % i ==0:
                sosu = False
        if sosu:
            answer+=1
    
    return answer