N,M = map(int,input().split())
li = [[0]*100 for i in range(100)] #그림의 가려진 횟수를 축적하기 위함이다.

for _ in range(N):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1-1,x2):
        for j in range(y1-1,y2): #가려질 때마다 1씩 횟수를 더힌디/
            li[i][j]+=1

cnt = 0
for i in range(100):
    for j in range(100):
        if li[i][j] > M: #가려진 회수가 M보다 많다면 안보이는 그림이다.
            cnt+=1

print(cnt)