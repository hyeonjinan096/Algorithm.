function solution(coin, cards) {
    var answer = 0;
    let num = cards.length
    let pass_num = num+1
    let my_cards = new Set(cards.slice(0,(num/3)))
    let next_cards = new Set([])
    cards = cards.slice(num/3)
    
    function isAble(cards1, cards2){
        for (let card of cards1){
            if (cards2.has(pass_num-card)){
                cards1.delete(card)
                cards2.delete(pass_num-card)
                return true
            }
        }
        return false
    }

    //라운드 돌리는 for문
    //종료 조건: 주어진 카드 없기 || 낼 카드 없거나
    let idx = 0
    while(1){
        answer+=1
        if (idx >= cards.length) break
        for(let i =0;i<2;i++){
            next_cards.add(cards[idx])
            idx++
        }
        
        if (isAble(my_cards, my_cards)){
            
        } else if (coin >=1 && isAble(my_cards, next_cards)){
            coin-=1
        } else if (coin >=2  && isAble(next_cards, next_cards)){
            coin-=2
        } else{
            break
        }
        
    }
    
    
    
    //라운드 할때 두개씩 카드 저장
    
    
    return answer;
}

//n장의 카드 -> n//3장을 뽑아 모두 가진다. 
//교환가능한 coin이 있다. 
//라운드 시작하다 두장 뽑음 
//카드 없으면 게임 종료 ,
//뽑은 카드에서 동전소모 카드 갖기
//카드 적힌 수의 합이 n+1이 되게 두장 내면 다음 라운드로 갈 수 있음 


    //도달 가능한 최대 라운드 수 겁나 다양한 수가 있습니다. 
    //당장에 사용되지는 않지만 나중에 한라운드를 갈 수 있는 카드가 있을 수 있습니다.
    //따라서 우리는 카드 갖을 수 있다면 경우의 수를 쟁여 둬야합니다. 
    //어떻게 쟁여둘 수 있을까요
    //또 신경써야할 부분은 코인을 최대한 아껴야한다는 점입니다. 
    //즉, 라운드를 최대한 가기 위해서는 
    //1. 카드를 적절히 선택할 수 있어야한다. 
    //2. 코인을 최대한 아껴야한다. 
    
    //그렇다면 
    //코인을 아끼는 경우를 찾아보아요 
    //1. 내 카드 안에서 해결되는 경우 (코인 0개 소모)
    //2. 내 카드와 외부 카드로 해결되는 경우 (코인 1개 소모)
    //3. 외부 카드로만 해결되는 경우(코인 2개 소모)
    
    //이를 위해 검사로직이 필요합니다. 
    //어차피 목표 값이 홀수여서 중복 체크를 할 필요는 없겠군요
    //이제 함수만 만들면 거의 됩니다
    //만들어 봅시다. 
    
    //함수 전 기본 동작 구현부터 해보겠습니다. 
