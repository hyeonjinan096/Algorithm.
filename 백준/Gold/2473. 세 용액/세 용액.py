import sys
input = sys.stdin.readline

N = int(input())
values = list(map(int,input().split()))
values.sort()

answer = [0,0,0]
Min = float('inf')
for i in range(N):
    start= i+1
    end = N-1

    while(start < end):
        Sum = values[i] + values[start] + values[end]

        if Min > abs(Sum):
            Min = abs(Sum)
            answer = [values[i],values[start],values[end]]

        if Sum > 0:
            end -= 1
        else:
            start += 1

print(*answer)