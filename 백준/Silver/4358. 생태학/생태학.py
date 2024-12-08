import sys

total = 0
dic = dict()
len = 0
while(1):
  word = sys.stdin.readline().rstrip()
  if word == '':
    break
  len+=1
  if word not in dic:
    dic[word] = 0
  dic[word]+=1


for k,v in dic.items():
  dic[k] = v/len * 100

sdic = dict(sorted(dic.items()))
for k,v in sdic.items():
  print("%s %.4f" %(k, v))
