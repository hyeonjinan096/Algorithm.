N, M = map(int, input().split())
lst = []
for i in range(1, N+1) :
    if N % i == 0 :
        lst.append(i)

if len(lst) < M :	
    print(0)
else :
    print(lst[M-1])	