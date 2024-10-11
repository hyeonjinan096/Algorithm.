def solution(n, k):
    answer = 0
    st = ''
    while(n):
        st = str(n%k) + st
        n //= k
    values=st.split('0')
    
    def check(n):
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
        
        return True
    
    for value in values:
        if value == '':
            continue

        value = int(value)
        if (value)<2:
            continue
        else:
            print(value, check(value))
            if check(value):
                answer+=1

    return answer