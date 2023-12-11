def solution(players, callings):
    pla_dic = {player: i for i , player in enumerate(players)}
    
    for p in callings: 
        i = pla_dic[p]
        pla_dic[p] -= 1
        pla_dic[players[i-1]] +=1
        players[i-1], players[i] =  players[i], players[i-1] 
    return players
