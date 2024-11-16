from collections import deque
N,M = map(int,input().split())
Max = 100001
dp = [float('inf')]*Max

def bfs():
  global N,M
  q = deque([N])
  dp[N] = 0

  while(q):
    cx = q.popleft()
    if cx == M:
      print(dp[M])
      return
    for nx in [cx-1,cx+1]:
      if 0<=nx<Max and dp[nx]>dp[cx]+1:
        dp[nx] = dp[cx]+1
        q.append(nx)
    if 0<=cx*2<Max and dp[cx*2]>dp[cx]:
      dp[cx*2] = dp[cx]
      q.append(cx*2)

bfs()



