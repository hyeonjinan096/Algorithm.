def solution(n, build_frame):
    answer = []
    
    def isOk():
        for x,y,a in answer:
            if a == 0: #기둥
                if y != 0 and [x,y,1] not in answer and [x-1,y,1] not in answer and [x,y-1,0] not in answer:
                    return False
            else:
                if [x,y-1,0] not in answer and [x+1,y-1,0] not in answer and not([x-1,y,1] in answer and [x+1,y,1] in answer):
                    return False
                
        return True
    
    for x,y,a,b in build_frame:
        if b == 1: #설치
            answer.append([x,y,a])
            if not isOk():
                answer.remove([x,y,a])
        else: #  삭제
            answer.remove([x,y,a])
            if not isOk():
                answer.append([x,y,a])
    
    answer.sort(key =lambda x:(x[0],x[1],x[2]))
    
    return answer