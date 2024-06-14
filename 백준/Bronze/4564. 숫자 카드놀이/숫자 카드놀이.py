while(1):
    n = input()
    if n == '0':
        break
    while(len(n)>1):
        print(n,end=' ')
        sum=1
        for i in n:
            sum *=int(i)
        n = str(sum)
    print(n)
