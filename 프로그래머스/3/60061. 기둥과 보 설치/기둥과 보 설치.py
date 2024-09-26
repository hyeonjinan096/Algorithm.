def solution(n, build_frame):
    result = []
    
    def check(result):
        for x,y,a in result:
            if a==0:
                if y!=0 and [x,y-1,0] not in result and [x,y,1] not in result and [x-1,y,1] not in result:
                    return False
            else:
                if [x,y-1,0] not in result and [x+1,y-1,0] not in result and not ([x-1,y,1] in result and [x+1,y,1] in result):
                    return False
        return True
    
    for x,y,a,b in build_frame:
        if b == 1:
            result.append([x,y,a])
            if not check(result):
                result.remove([x,y,a])
        else:
            if [x,y,a] in result:
                result.remove([x,y,a])
            if not check(result):
                result.append([x,y,a])
        
    result.sort(key=lambda x:(x[0],x[1],x[2]))
    
    return result

