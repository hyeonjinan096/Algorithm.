n,w,h,l=map(int,input().split())
w//=l
h//=l
sum=w*h
if n>=sum: print(sum)
else: print(n)