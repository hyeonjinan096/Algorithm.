import sys
from heapq import heappush, heappop
t = int(input())
q = []
for _ in range(t):
  n = int(sys.stdin.readline())
  if n != 0:
    heappush(q,n)
  else:
    if len(q)>0:
      print(heappop(q))
    else:
      print(0)