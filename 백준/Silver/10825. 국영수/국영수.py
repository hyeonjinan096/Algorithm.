n = int(input())
lst = [list(input().split()) for _ in range(n)]

lst.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

#print(*list(lst[i][0] for i in range(n)))

for i in range(n):
    print(lst[i][0])