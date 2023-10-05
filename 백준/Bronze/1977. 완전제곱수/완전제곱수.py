m = int(input())
n = int(input())

list = []
i = 1

while i**2 <= n:
  if m <= i**2 <= n:
    list.append(i**2)
  i+=1
  
if list == []:
  print(-1)

else:
  print(sum(list))
  print(list[0])