ls = list(map(int,input().split()))

while(1):
    if(ls==[1,2,3,4,5]):
        break
    for i in range(4):
        if ls[i] > ls[i+1]:
            ls[i], ls[i+1] = ls[i+1], ls[i]
            print(*ls)
