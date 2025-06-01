import sys

input = sys.stdin.readline

N,M = map(int,input().split())
lst = list(map(int,input().split()))

S = [0] * (N+1)

for i in range(1,N+1):
  S[i] = (S[i-1] + lst[i-1])

for i in range(M):
  a,b = map(int,input().split())
  print(S[b] - S[a] + lst[a-1])
