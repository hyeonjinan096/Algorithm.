n = int(input()) 

count = 0
z = 1 

while n > 0:
    if z > n:       
        z = 1      
    n -= z       
    z += 1        
    count += 1
    
print(count)