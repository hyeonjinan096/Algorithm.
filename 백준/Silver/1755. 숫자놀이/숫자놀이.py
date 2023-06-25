import sys

a, b = map(int,sys.stdin.readline().strip().split())

d = {1:'one', 2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'zero' }

n =0
m =0
dic ={}
for i in range(a,b+1):
    n = i//10
    m = i%10
    if(n>0):
        str = d[n]+d[m]
    else:
        str = d[m]
    dic[i]=str

s = sorted(dic,key=lambda x:dic[x])
for i in range(len(s)):
    if(i%10 ==0 and i!=0):
        print()
    print(s[i], end=" ")



