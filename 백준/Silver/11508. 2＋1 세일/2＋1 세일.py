n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
l.sort(reverse=True)

result=0
for i in range(2,len(l),3):
    result+=l[i]

print(sum(l)-result)