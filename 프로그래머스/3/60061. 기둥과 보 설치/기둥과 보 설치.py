def solution(n, build_frame):
    answer = []
    
    def isChecked(answer):

        for x,y,a in answer:
        #기둥
            if(a==0):
                if(y!=0 and [x-1,y,1] not in answer and [x,y,1] not in answer and [x,y-1,0] not in answer):
                    return False

            if(a==1):
                if([x,y-1,0] not in answer and [x+1,y-1,0] not in answer and 
                 not([x-1,y,1] in answer and [x+1,y,1] in answer) 
                  ):
                    return False
            
        return True
    
    
    for x,y,a,b in build_frame:
        if b==0 and [x,y,a] in answer:
            answer.remove([x,y,a])
            if not isChecked(answer):
                answer.append([x,y,a])
        elif b==1 and [x,y,a] not in answer:
            answer.append([x,y,a])
            if not isChecked(answer):
                answer.remove([x,y,a])
        
        answer.sort(key=lambda x:(x[0],x[1],x[2]))
                
    return answer