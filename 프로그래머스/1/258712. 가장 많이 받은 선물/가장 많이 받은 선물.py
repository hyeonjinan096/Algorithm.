def solution(friends, gifts):
    answer = 0
    #가장 많은 선물을 받은 친구가 받은 선물 수 
    #많이 준 애가 받음 
    #같으면 선물 지수 큰 사람이 받음
    #둘 다 같으면 선물 주고 받지 않음 
    
    #선물 표 만들기 
    
    #선물 지수 계산하기 
    #준 선물 - 받은 선물
    table = [[0]*len(friends) for _ in range(len(friends))]
    giftnum = [0]*len(friends)
    for gift in gifts:
        T, F = gift.split(' ')
        t = friends.index(T)
        f = friends.index(F)
        table[t][f] +=1
        giftnum[t]+=1
        giftnum[f]-=1
    
    answer = [0]*len(friends)
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            if table[i][j] > table[j][i]:
                answer[i]+=1
            elif table[i][j] < table[j][i]:
                answer[j]+=1
            elif giftnum[i] > giftnum[j]:
                answer[i]+=1
            elif giftnum[i] < giftnum[j]:
                answer[j]+=1
    
    return max(answer)