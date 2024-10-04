import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

cnt = 0
for i in range(n):
  goal = arr[i]
  tmp = arr[:i] + arr[i + 1:]
  start = 0
  end = len(tmp)-1
  while start < end:
    Sum = tmp[start] + tmp[end]
    if Sum == goal:
      cnt+=1
      break
    elif Sum > goal:
      end-=1
    elif Sum < goal:
      start+=1

print(cnt)
       