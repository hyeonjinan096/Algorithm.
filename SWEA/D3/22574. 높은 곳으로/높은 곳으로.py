#import sys
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  N,P = map(int,input().split(" "))

  answer = 0
  for i in range(0,N+1):
    answer+=i
    if answer == P:
      answer -=1
  print(answer)




