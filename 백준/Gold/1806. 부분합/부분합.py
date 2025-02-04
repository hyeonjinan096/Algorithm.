N,S = map(int,input().split())
values = list(map(int,input().split()))

right, left = 0, 0
Sum = 0
min_sum = float('inf')

while(1):
    if Sum >= S:
        min_sum= min(min_sum, right-left)
        Sum -= values[left]
        left+=1
        continue
    if right == N:
        break
    if Sum < S:
        Sum += values[right]
        right += 1

if min_sum == float('inf'): print(0)
else:
    print(min_sum)
