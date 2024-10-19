import sys

N = int(input())
dic = []

def pushInDic(w):
  dic.append(w)
  if 'A'<=w<='Z':
    dic.append(chr(ord(w)+32))
  else:
    dic.append(chr(ord(w)-32))

for _ in range(N):
  word = sys.stdin.readline().rstrip()
  flag = 0
  result = []

  for i in range(len(word)):
    if i == 0 or word[i-1] == ' ':
      if word[i] != ' ' and  word[i] not in dic and flag == 0:
        pushInDic(word[i])
        result.append('['+word[i]+']')
        flag = 1
      else:
        result.append(word[i])
    else:
      result.append(word[i])
  
  if flag == 0:
    result = []
    for w in word:
      if flag ==0 and w not in dic and w != ' ':
        flag = 1
        pushInDic(w)
        result.append('['+w+']')
      else:
        result.append(w)
        

  print(*result,sep='')
  



