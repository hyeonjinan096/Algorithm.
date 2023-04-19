import sys
n = int(sys.stdin.readline())
s =[0]*n
for i in range(n):
    s[i] = int(sys.stdin.readline())
    
s.sort()
for i in range(n):
    print(s[i])
