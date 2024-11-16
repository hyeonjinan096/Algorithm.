from collections import deque
import sys

N,M = map(int,sys.stdin.readline().split())
Max = 100001
dp = [0]*Max
move = [0]*Max

def print_move(x):
  data = []
  tmp = x
  for _ in range(dp[x]+1):
    data.append(tmp)
    tmp = move[tmp]
  print(' '.join(map(str,data[::-1])))

def bfs(x):
  q = deque([x])
  while(q):
    cx = q.popleft()
    if cx == M:
      print(dp[cx])
      print_move(cx)
      return
    for i in [cx-1,cx+1,cx*2]:
      if 0<=i<Max and dp[i] ==0:
        dp[i] = dp[cx]+1
        q.append(i)
        move[i] = cx

dp[N] = 0
bfs(N)

