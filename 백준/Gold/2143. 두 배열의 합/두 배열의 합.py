T = int(input())
a = int(input())
lst_a = list(map(int,input().split()))
b = int(input())
lst_b = list(map(int,input().split()))


dic_a = {}
for i in range(a):
    sum = 0
    for j in range(i,-1,-1):
        sum+= lst_a[j]
        if sum not in dic_a:
            dic_a[sum] = 0
        dic_a[sum] += 1

dic_b = {}
for i in range(b):
    sum = 0
    for j in range(i,-1,-1):
        sum+= lst_b[j]
        if sum not in dic_b:
            dic_b[sum] = 0
        dic_b[sum] += 1


answer = 0
for key,value in dic_a.items():
    if T-key in dic_b:
        answer += (dic_b[T-key] * value)

print(answer)
        
