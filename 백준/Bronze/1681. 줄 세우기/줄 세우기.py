N,l = list(map(int,input().split(' ')))
l = str(l)
num = 1
C = 0	

while True:
    if str(l) not in str(num): 
        C+=1	
        if C == N:
            print(num)
            break
        num+=1
        
    else:	
        num+=1	