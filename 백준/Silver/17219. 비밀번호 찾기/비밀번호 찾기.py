n ,m = map(int,input().split())
dic ={}
for i in range(n):
	k,v = map(str,input().split())
	dic[k] = v
for i in range(m):
	k = input()
	print(dic[k])