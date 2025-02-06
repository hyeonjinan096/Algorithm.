N = int(input())
values = list(map(int,input().split()))

L = 0
R = N-1

answer =[]
zero_v = float('inf')

while(L < R):
    v = values[L] + values[R]
    if abs(v) < zero_v:
        zero_v = abs(v)
        answer = [values[L],values[R]]
        if zero_v == 0:
            break
    
    if abs(values[L] + values[R-1]) < abs(values[L+1] + values[R]):
        R-=1
    else:
        L+=1

print(*answer)
