from collections import deque
N, K = map(int, input().split())
Max = 100001
values = [float("inf")]*Max

def bfs(start, end):
  q = deque([start])
  values[start] = 0

  while(q):
    e = q.popleft()
    time = values[e]

    if e == end:
      return time
    
    for idx in [e-1,e+1]:
      if 0<=idx<Max and values[idx]>time+1:
        values[idx] = time+1
        q.append(idx)
    if 0<=e*2<Max and values[e*2]>time:
      values[e*2] = time
      q.append(e*2)
  
print(bfs(N,K))