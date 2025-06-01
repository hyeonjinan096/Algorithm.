N, M = map(int,input().split())
lst = list(map(int,input().split()))

left = 0
Sum = 0
answer = float("inf")

for right in range(0,N):
    Sum += lst[right]

    while Sum >= M:
        answer = min(answer, right-left+1)
        Sum-=lst[left]
        left+=1

if answer == float("inf"):
  print(0)
else:
  print(answer)