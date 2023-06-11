import sys

word = sys.stdin.readline().upper().strip()

list = list(set(word))
#upper대분자화
#set함수 중복된 문자값을 제거한 후 변수에 저장

cnt = []
for i in list:
  count = word.count
  cnt.append(count(i)) #사용 횟수 담기

if cnt.count(max(cnt)) > 1:  #사용 횟수 많은게 여러개면 ?출력
  print("?")

else:
  print(list[(cnt.index(max(cnt)))])