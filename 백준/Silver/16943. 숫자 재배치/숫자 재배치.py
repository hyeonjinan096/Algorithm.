from itertools import permutations

a, b = input().split() #문자열로 받음

b = int(b) # 숫자로 변환
c = -1 #초기화 숫자

a_list = []
for item in permutations(a): #문자열의 순열 구함
    a_list.append(''.join(item)) #다시 문자열로 변환

for i in a_list: 
    if i[0] == '0':
        continue
    i = int(i)
    if i < b:
        c = max(c,i)

print(c)