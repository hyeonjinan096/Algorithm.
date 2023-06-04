import sys
n = int(sys.stdin.readline()) 
a = 2*n 

for i in range(1, a): 
  if i <= n : 
    print("*"*(i) + ' '*(a-2*i) + '*'*(i))
  else: 
    print("*"*(a-i) + " "*(a-2*(a-i))+ '*'*(a-i)) 