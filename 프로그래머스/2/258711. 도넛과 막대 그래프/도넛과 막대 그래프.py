def solution(edges):
    answer = [0,0,0,0]
    
    exchanges = {}
    for a,b in edges:
        if a not in exchanges:
            exchanges[a] = [0,0]
        if b not in exchanges:
            exchanges[b] = [0,0]
        exchanges[a][0] +=1
        exchanges[b][1] +=1
    
    for key, [o, i] in exchanges.items():
        if o>=2 and i == 0:
            answer[0] = key
        elif o == 0 and i > 0:
            answer[2] +=1
        elif o>=2 and i>=2:
            answer[3] +=1
    answer[1] = (exchanges[answer[0]][0] - answer[2]-answer[3])
    
    return answer