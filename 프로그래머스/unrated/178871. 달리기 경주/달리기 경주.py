def solution(players, callings):
    idx = {i: player for i ,player in enumerate(players)}
    p = {player:i for i, player in enumerate(players)}
    
    for call in callings:
        loc = p[call] #호명한 선수의 등수
        loc2 = loc-1 #앞 선수 등수
        
        idx[loc] = idx[loc2]
        idx[loc2] = call
        p[call] = loc2
        p[idx[loc]] = loc
        
    return list(idx.values())