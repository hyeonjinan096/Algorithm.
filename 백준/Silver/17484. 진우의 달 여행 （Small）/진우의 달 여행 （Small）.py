import sys
from collections import deque

N,M = map(int,input().split())
fuel_list = [list(map(int,input().split())) for _ in range(N)]
min_fuel_list = [[[float('inf')]*3 for _ in range(M)] for _ in range(N)]

for i in range(M):
  min_fuel_list[0][i] = [fuel_list[0][i]]*3

for i in range(1,N):
  for j in range(M):
    for k in range(3):
      if (j == 0 and k == 2) or (j == M-1 and k == 0):
        continue
      for l in range(3):
        if k == l:
          continue
        min_fuel_list[i][j][k] = min(min_fuel_list[i][j][k], min_fuel_list[i-1][j-k+1][l] + fuel_list[i][j])


answer = float('inf')
for i in range(M):
  answer = min(min(min_fuel_list[N-1][i]),answer)
print(answer)