N,M = map(int,input().split())
lst = list(map(int,input().split()))

left = 0
Sum = 0
cnt = 0

for right in range(N):
  Sum += lst[right]
  while(Sum > M):
    Sum -= lst[left]
    left+=1
  if Sum == M:
    cnt+=1

print(cnt)