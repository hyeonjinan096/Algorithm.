from collections import deque
N, K = map(int, input().split())
Max = 100001
values = [float("inf")]*Max

def bfs(end):
  q = deque([end])
  values[end] = 0
  
  while(q):
    e=q.popleft()
    time = values[e]

    if e == N:
      return time

    if 0<=e-1<Max and values[e-1]>time+1:
      values[e-1] = time+1
      q.append(e-1)
    if 0<=e+1<Max and values[e+1]>time+1:
      values[e+1] = time+1
      q.append(e+1)
    if e%2 ==0 and 0<=e//2<Max and values[e//2]>time:
      values[e//2] = time
      q.append(e//2)


print(bfs(K))