n = int(input())
values = list(map(int,input().split()))

#start, end
answer = float('inf')
start, end = 0,n-1
while(start < end):
    result = values[start] + values[end]
    if abs(result) < abs(answer):
        answer = result

    if result > 0:
        end-=1
    elif result <0:
        start+=1
    else:
        break

print(answer)