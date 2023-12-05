N = int(input())    
first = list(map(int, input().split()))  
second = list(map(int, input().split()))
 
sum = 0
for i in first:
    sum += abs(i)
 
for j in second:
    sum += abs(j)
 
print(sum)