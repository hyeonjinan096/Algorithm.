from itertools import combinations
n = int(input())
values = list(map(int,input().split()))
x = int(input())

values.sort()
s =0
e =n-1
answer =0

while(s<e):
    if values[s] + values[e] == x:
        answer+=1
        s+=1
        e-=1
    elif values[s] + values[e] < x:
        s+=1
    else:
        e-=1
print(answer)