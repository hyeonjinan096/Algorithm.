n, s, p = map(int, input().split())
if n!=0:
    score = list(map(int, input().split()))
    if n == p and s<=score[-1]:
        print(-1)
    else:
        res = n + 1
        for i in range(n):
            if  s>=score[i] :
                res = i + 1
                break
        print(res)
else:
    print(1)