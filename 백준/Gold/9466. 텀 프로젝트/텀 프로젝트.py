from collections import deque
import sys
sys.setrecursionlimit(111111)

T = int(sys.stdin.readline())
for _ in range(T):
  N = int(sys.stdin.readline())
  numbers = [0] + list(map(int,sys.stdin.readline().split()))
  visited = [True] + [False]*N
  answer = []

  def dfs(x):
    global answer
    visited[x] = True
    cycle.append(x)
    number = numbers[x]

    if visited[number]:
      if number in cycle:
        answer += cycle[cycle.index(number):] 
        return
    else:
      dfs(number)


  for i in range(1,N+1):
    if not visited[i]:
      cycle = []
      dfs(i)

  print(N - len(answer))

  