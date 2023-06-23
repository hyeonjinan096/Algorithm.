import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
count =0
n,i =0,0
l= len(b)

while(i<len(a)):
    s = a[i:i+l]
    n =1
    if(s == b):
        count+=1
        n = len(b)
    i+=n
print(count)