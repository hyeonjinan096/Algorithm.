import sys
from collections import deque
N,d,k,c = map(int,input().split())
lst = []
for i in range(N):
    lst.append(int(input()))
lst += lst

select_lst = deque(lst[:k])

tmp = set(select_lst)
tmp.add(c)
max = len(tmp)


for i in range(0,N):
    if i+k > N*2:
        break
    select_lst.popleft()
    select_lst += [lst[i+k]]
    tmp = set(select_lst)
    tmp.add(c)
    if len(tmp) > max:
        max = len(tmp)

print(max)

