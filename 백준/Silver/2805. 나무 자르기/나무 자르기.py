import sys

input = sys.stdin.readline

N, M = map(int,input().split())
tree = list(map(int,input().split()))


right = max(tree) 
left = 0
result = 0

while(left <= right):
    mid = (left + right)//2
    Sum = 0
    for i in tree:
      if i > mid:
        Sum += i - mid

    if Sum >= M:
      result = mid
      left = mid +1
    else:
      right = mid -1
      

print(result)  
    
