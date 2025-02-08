N,S = map(int,input().split())
lst = list(map(int,input().split()))

l,r = 0,0
Min = float('inf')
Sum = 0
while(1):
    if Sum >= S:
        Min = min(r-l, Min)
        Sum -= lst[l]
        l+=1
    elif r >= N:
        break
    else:
        Sum += lst[r]
        r+=1

if Min == float('inf'):
    print(0)
else:
    print(Min)