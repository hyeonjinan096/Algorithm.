import sys
n = int(sys.stdin.readline())
s =[]
for i in range(n):
    a,b = map(str,sys.stdin.readline().split())
    s.append([int(a),b])  #숫자 문자열 리스트에 같이 담을 수 있음

s.sort(key = lambda x : x[0])  ##(age,name)에서 age만 비교함
for i in range(n):
    print(*s[i])  #*붙이면 형식 없애줌