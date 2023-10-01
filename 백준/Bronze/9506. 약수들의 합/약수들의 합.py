while (1):
    n = int(input()) 
    if n==-1:
        break  
        
    list=[]  
    for i in range(1,n+1):
        if n%i==0: 
            list.append(i)  
 
    S=0 
    idx=list[len(list)-1]  
    for i in list[:-1]:
        S+=i  
    if S==idx:  
        answer=str(idx)+" = "+str(list[0])
        for i in range(1,len(list)-1):
            answer+=" + "+str(list[i])
        print(answer)
    else:  
        print(str(list[-1])+" is NOT perfect.")