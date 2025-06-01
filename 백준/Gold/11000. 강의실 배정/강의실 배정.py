from heapq import heappop, heappush
import sys

input = sys.stdin.readline

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
lst.sort()

q = []

for start, end in lst:
    if q and q[0] <= start:
        heappop(q)
    heappush(q, end)

print(len(q))
        
