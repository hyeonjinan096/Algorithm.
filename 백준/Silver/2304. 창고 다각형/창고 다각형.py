N = int(input())
lst = []
max_l, max_h = 0,0
for _ in range(N):
  l,h = map(int,input().split())
  lst.append([l,h])
  if max_h < h:
    max_h, max_l = h,l

lst.sort(key=lambda x:x[0])
max_i = lst.index([max_l,max_h])

answer = max_h

std_h = lst[0][1]
for i in range(0,max_i):
  cur_l, cur_h = lst[i]
  if cur_h > std_h:
    std_h = cur_h
  answer+=(lst[i+1][0]-lst[i][0])*std_h

std_h = lst[-1][1]
for i in range(N-1,max_i,-1):
  cur_l, cur_h = lst[i]
  if cur_h > std_h:
    std_h = cur_h
  answer+=(lst[i][0]-lst[i-1][0])*std_h

print(answer)



