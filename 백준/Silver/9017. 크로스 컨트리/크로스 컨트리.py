import sys

T = int(input())
for i in range(T):
  N = int(input())
  values = list(map(int,sys.stdin.readline().split(' ')))
  dic = {}

  for value in values:
    if value not in dic:
      dic[value] = {'score':0,'score_cnt':0,'All_cnt':0,'five':0}
    dic[value]['All_cnt']+=1

  s = 1
  for value in values:
    if dic[value]['All_cnt'] < 6:
      continue
    dic[value]['score_cnt']+=1
    if dic[value]['score_cnt'] == 5:
      dic[value]['five']= s
    if dic[value]['score_cnt']<5:
      dic[value]['score']+=s
    s+=1

  dic[-1] = {'score':float('inf'),'cnt':float('inf'),'five':float('inf'),'All_cnt':float('inf')}
  answer = -1

  for team,value in dic.items():
    if value['All_cnt'] < 6:
      continue
    if value['score'] < dic[answer]['score']:
      answer = team
    elif value['score'] == dic[answer]['score'] and value['five'] < dic[answer]['five']:
      answer = team

  print(answer)
