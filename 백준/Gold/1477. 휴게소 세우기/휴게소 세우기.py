import sys
input = sys.stdin.readline

N,M, L = map(int,input().split())
lst = list(map(int,input().split()))
lst.append(0)
lst.append(L)
lst.sort()

left,right = 1,L
answer = 0

while left <= right:
    mid = (left + right) //2
    count = 0

    for i in range(1,len(lst)):
        distance = lst[i] - lst[i-1]
        count += (distance - 1)//mid

    if count > M:
        left = mid + 1
    else:
        answer = mid
        right = mid -1

print(answer)