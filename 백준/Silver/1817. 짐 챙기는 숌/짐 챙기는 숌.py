n,m = map(int, input().split())
if n != 0:
    weight = list(map(int,input().split()))

answer =0
sum =0
for i in range(n):
    sum +=weight[i]
    if sum>m :
        answer+=1
        sum = weight[i]
    elif sum ==m:
        answer+=1
        sum = 0
if sum > 0:
    answer+=1

print(answer,end='')