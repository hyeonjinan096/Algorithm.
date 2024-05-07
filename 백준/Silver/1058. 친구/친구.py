n = int(input())
lst = [[] for _ in range(n)]
lst2 = [[] for _ in range(n)]

for i in range(n):
    s = input()
    for j in range(n):
        if s[j] == 'Y':
            lst[i].append(j)
            lst2[i].append(j)

for i in range(n):
    for j in lst[i]:
        #print(j)
        for k in lst[j]:
            if k != i and k not in lst2[i]:
                lst2[i].append(k)

answer =[]
for i in lst2:
    answer.append(len(i))
print(max(answer))
