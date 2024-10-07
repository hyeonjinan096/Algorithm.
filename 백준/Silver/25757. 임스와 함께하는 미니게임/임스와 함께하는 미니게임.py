import math

dic = {
  "Y":2,
  "F":3,
  "O":4
}

N,G = input().split()
N = int(N)
num = dic[G]
players = set([])
for i in range(N):
  players.add(input())

print(len(players)//(num-1))
