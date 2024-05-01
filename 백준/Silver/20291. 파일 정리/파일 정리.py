n = int(input())
dic = {}
for i in range(n):
    name,file = input().split('.')
    if file in dic:
        dic[file]+=1
    else:
        dic[file] =1

dic = sorted(dic.items())
for i in dic:
    print(i[0],i[1])

