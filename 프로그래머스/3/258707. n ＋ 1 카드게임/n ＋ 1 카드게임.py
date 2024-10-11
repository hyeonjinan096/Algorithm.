def solution(coin, cards):
    n = len(cards)
    key = n+1
    
    def check(cards1, cards2):
        for card in cards1:
            if key-card in cards2:
                cards1.remove(card)
                cards2.remove(key-card)
                return True
        return False

    mycards = cards[:n//3]
    nextcards = []
    idx = n//3
    Round = 0
    
    while(1):
        Round+=1
        if idx+1 >= n:
            break
        for _ in range(2):
            nextcards.append(cards[idx])
            idx+=1
    
        if(check(mycards, mycards)):
            continue
        elif(coin>0 and check(mycards, nextcards)):
            coin-=1
        elif(coin>1 and check(nextcards, nextcards)):
            coin-=2
        else:
            break
        
            
            
    
    
    return Round