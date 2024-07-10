for i in range(int(input())):
    n=int(input())
    count=2
    answer = 0
    while n!=1:
        if n%count==0:
            n//=count
            answer+=1
        else:
            if answer==0:
                pass
            else:
                print(count,answer)
            answer=0
            count+=1
    print(count,answer)