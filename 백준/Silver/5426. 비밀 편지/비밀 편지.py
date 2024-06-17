t = int(input())
for _ in range(t):
    lst = input()
    l = int(len(lst)**(1/2))
    for i in range(l-1,-1,-1):
        x = i
        print(lst[x],end='')
        for j in range(l-1):
            x+=l
            print(lst[x],end='')
    print('')
