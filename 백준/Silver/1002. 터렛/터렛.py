n = int(input())

for i in range(n):
    values = list(map(int,input().split()))
    m = abs(values[2] - values[5])
    M = values[2] + values[5]
    d = ((values[0]-values[3])**2 + (values[1]-values[4])**2)**(1/2)

    if d == 0:
        if m == 0:
            print(-1)
        else:
            print(0)
    elif d == m or d == M:
        print(1)
    elif m<d <M:
        print(2)
    else:
        print(0)




