def solution(edges):
    answer = [0,0,0,0]
    info = {}
    for x,y in edges:
        if x not in info:
            info[x] = [0,0] #out, in
        if y not in info:
            info[y] = [0,0]
        info[x][0]+=1
        info[y][1]+=1
    
    for v, [o,i] in info.items():
        if i == 0 and o>=2:
            answer[0] = v
        elif i>=2 and o>=2:
            answer[3] += 1
        elif i>0 and o==0:
            answer[2]+=1
    answer[1] = info[answer[0]][0] - answer[2] - answer[3] 
    
    return answer