def delete_card(a,b,t):
    for i in a:
        if t-i in b:
            a.remove(i)
            b.remove(t-i)
            return True
    return False

def solution(coin, cards):
    answer = 1
    n = len(cards)
    mycard = [cards[i] for i in range(n//3)]
    index=n//3
    nextcards=[]
    
    while coin>=0 and index<n:
        nextcards.append(cards[index])
        nextcards.append(cards[index+1])
        if delete_card(mycard,mycard, n+1):
            pass
        elif coin>=1 and delete_card(mycard, nextcards, n+1):
            coin-=1
        elif coin>=2 and delete_card(nextcards, nextcards, n+1):
            coin-=2
        else:
            break
            
        answer+=1
        index+=2
    return answer