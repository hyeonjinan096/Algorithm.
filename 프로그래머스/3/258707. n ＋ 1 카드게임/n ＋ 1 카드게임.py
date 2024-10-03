def solution(coin, cards):
    Round = 0
    n = len(cards)
    N = n+1
    mycard = cards[:n//3]
    idx = n//3
    
    def check(a, b):
        for i in a:
            if N-i in b:
                a.remove(i)
                b.remove(N-i)
                return True
        return False
    
    nextcard = []
    while(1):
        Round+=1
        if idx == len(cards):
            break

        for _ in range(2):
            nextcard.append(cards[idx])
            idx+=1
        if check(mycard, mycard):
            continue
        elif coin-1>=0 and check(mycard,nextcard):
            coin-=1
        elif coin-2>=0 and check(nextcard, nextcard):
            coin-=2
        else:
            break  
        
    
    return Round