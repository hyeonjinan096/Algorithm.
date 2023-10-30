day = int(input())
car = list(map(int, input().split()))

cnt =0
for i in range(len(car)):
  if car[i] == day:
    cnt+=1
  else:
    continue

print(cnt)