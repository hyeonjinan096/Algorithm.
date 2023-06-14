def solution(players, callings):
    p = {p : i for i , p in enumerate(players)}
    
    for call in callings:
        idx = p[call] 
    
        a = players[idx-1]
        players[idx-1] =players[idx]
        players[idx] = a
        
        p[call] = idx-1
        p[a] = idx
        
    return players