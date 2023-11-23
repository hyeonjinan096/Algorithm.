list = []

for i in range(6):  
    list.append(int(input())) 
    
a = sorted(list[:4]) 
b = sorted(list[4:]) 

print(sum(a[1:]) + b[-1])