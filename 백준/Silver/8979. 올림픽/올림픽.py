N,M = map(int,input().split())

arr = []
for _ in range(N):
    i, g,s,c = map(int,input().split())
    arr.append([i,g,s,c])

arr.sort(key= lambda x:[x[1],x[2],x[3]], reverse= True)

l = 1
obj = {arr[0][0]:l}

for i in range(1,N):
    if (arr[i-1][1] != arr[i][1] or arr[i-1][2] != arr[i][2] or arr[i-1][3] != arr[i][3]):
        l+=1
    obj[arr[i][0]] = l

print(obj[M])