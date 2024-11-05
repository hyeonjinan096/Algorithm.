import sys

N,M = map(int,sys.stdin.readline().split(' '))
dic = {}
for _ in range(N):
  word = sys.stdin.readline().strip()
  if len(word) < M:
    continue 
  if word not in dic:
    dic[word] = 1
  dic[word]+=1

Array = sorted(dic.items(), key=lambda x: (-x[1],-len(x[0]),x[0]))

answer = []
for x,y in Array:
  print(x)