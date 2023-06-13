import sys
A,B = sys.stdin.readline().strip().split()

count =0
min = len(B)
for i in range(len(B)-len(A)+1):
    count =0
    for j in range(len(A)):
        if(A[j]!=B[i+j] and i+j < len(B)):
            count+=1
    if(min>count):
        min =count
   
print(min)

