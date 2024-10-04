def solution(coin, cards):
    Round = 0#라운드 수 
    n = len(cards)
    key = n+1 

    mycard = cards[:n//3]
    nextcard = []
    

    def check (cards1, cards2):
        for card in cards1:
            if key - card in cards2:
                cards2.remove(key-card)
                cards1.remove(card)
                return True
        return False
    
    idx = n//3
    while(1):
        Round+=1
        if idx == len(cards):
            break
        
        for _ in range(2):
            nextcard.append(cards[idx])
            idx+=1

        if check(mycard, mycard):
            continue
        elif coin>=1 and check(mycard, nextcard):
            coin-=1
        elif coin>=2 and check(nextcard, nextcard):
            coin-=2
        else:
            break
    
    return Round