import sys
n = int(sys.stdin.readline())
R=[]
for i in range(n):
    r,g,b = map(int,sys.stdin.readline().strip().split()) #strip왼쪽 공백 제거

    if(i==0):
        R=[r,g,b]
        continue
    R = [min(R[1], R[2]) + r, 
           min(R[0], R[2]) + g,
           min(R[0], R[1]) + b]
    
print(min(R))