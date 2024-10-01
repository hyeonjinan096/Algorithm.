def solution(n, build_frame):
    answer = [[]]
    build = []
    
    def isOk():
        nonlocal build
        for x,y,a in build:
            if a== 0:
                if y != 0 and [x,y,1] not in build and [x-1,y,1] not in build and [x,y-1,0] not in build:
                    return False
            else:
                if [x,y-1,0] not in build and [x+1,y-1,0] not in build and not ([x-1,y,1] in build and [x+1,y,1] in build):
                    return False
        return True
                    
        
    
    for x,y,a,b in build_frame:
        if b == 1:
            build.append([x,y,a])
            if not isOk():
                build.remove([x,y,a])
        else:
            if [x,y,a] not in build:
                continue
            build.remove([x,y,a])
            if not isOk():
                build.append([x,y,a])
                
    build.sort(key=lambda x:(x[0],x[1],x[2]))
    
    
    return build

