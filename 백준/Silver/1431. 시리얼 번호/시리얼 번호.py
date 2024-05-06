n = int(input())
values =[[0,0,0] for _ in range(n)]

for i in range(n):
    values[i][0] = input()
for i in range(n):
    values[i][1] = len(values[i][0])
for i in range(n):
    sum = 0
    for j in values[i][0]:
        if '0'<=j<='9': #숫자 판별 식 알아보기
            sum+=int(j)
    values[i][2] = sum
values.sort(key = lambda x:(x[1],x[2],x[0]))

for i in values:
    print(i[0])
