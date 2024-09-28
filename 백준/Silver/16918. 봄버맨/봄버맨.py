import copy
R,C,N = map(int,input().split())
value = [list(input()) for _ in range(R)]
All = [['O']*C for i in range(R)]
answer = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def destory(x,y):
  global answer, value
  answer[x][y] = "."
  for i in range(4):
    if 0<=x+dx[i]<R and 0<=y+dy[i]<C:
      answer[x+dx[i]][y+dy[i]] = "."


if N<2: #0,1 같아야함
  answer = value
elif N %2 ==0:
  answer = All
else: # 그 이후 2에서 All 및 저장, 홀수 일 경우 value기분 터져야함
  for i in range(2,N+1):
    if i%2 != 0:
      answer = copy.deepcopy(All)
      for x in range(R):
        for y in range(C):
          if value[x][y] == 'O':
            destory(x,y) #여기서 제거가 되는 거는 value에서도 제거
      value = copy.deepcopy(answer)


for i in answer:
    print(''.join(i))




