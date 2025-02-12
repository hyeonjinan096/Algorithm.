N = int(input())
arr = []
for _ in range(N):
    x,y = map(int,input().split())
    arr.append([x,y])
arr.sort(key = lambda x:x[0])

answer = 0
dp = []
for i in range(N):
    if len(dp) == 0 or dp[-1] < arr[i][1]:
        if arr[i][1] != 0:
            dp.append(arr[i][1])
    else:
        while(dp and dp[-1] > arr[i][1]):
            dp.pop()
            answer+=1
        if arr[i][1] == 0:
            continue
        if len(dp) == 0 or dp[-1] != arr[i][1]:
            dp.append(arr[i][1])

print(answer + len(dp))


