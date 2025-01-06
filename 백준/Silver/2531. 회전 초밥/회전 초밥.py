import sys
from collections import deque
N,d,k,c = map(int,input().split())
lst = []
for i in range(N):
    lst.append(int(input()))
lst += lst

select_lst = deque(lst[:k])

max = len(set(select_lst))
if c in select_lst:
    max-=1


for i in range(0,N):
    if i+k > N*2:
        break
    select_lst.popleft()
    select_lst += [lst[i+k]]
    length = len(set(select_lst))
    if c in select_lst:
        length-=1
    if length > max:
        max = length

print(max + 1)

