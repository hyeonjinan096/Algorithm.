n = int(input())
lst = list(input())
answer =0

for i in range(n):
    if lst[i] == 'E' and i+1 < n and lst[i+1] == 'W':
        answer+=1
if answer ==0:
    answer = n
print(answer)