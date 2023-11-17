Condos = []
for i in range(int(input())):
    l, p = map(int, input().split())
    Condos.append([l, p])
Condos.sort()

cost = 10001
result = 0
for i in Condos:
    temp = i[1]
    if temp < cost:
        cost = temp
        result += 1
print(result)