import sys

N,M = map(int,input().split())
dic = set([sys.stdin.readline().rstrip() for _ in range(N)])
sets = set()
cnt = N

for _ in range(M): 
  values = sys.stdin.readline().rstrip().split(',')
  dic -= set(values)
  print(len(dic))
