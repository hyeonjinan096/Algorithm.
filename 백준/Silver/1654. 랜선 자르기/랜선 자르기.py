import sys
input = sys.stdin.readline

K,N = map(int,input().split())
values = [int(input()) for _ in range(K)]
values.sort(reverse = True)

answer = 0
start = 1
end = values[0]
while(start <= end):
    mid = (start + end) // 2
    cnt = 0
    for value in values:
        cnt += value // mid

    if cnt < N:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)