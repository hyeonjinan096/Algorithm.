# 3:22

N, a, b = map(int,input().split())
flag = 0
if b > a:
    a,b = b,a
    flag = 1

a_arr = []
b_arr = []
answer = 0

for i in range(1,a+1):
    a_arr.append(i)

for j in range(1,b):
    b_arr.append(j)

arr = a_arr + b_arr[::-1]
if flag:
    arr = arr[::-1]

if N < len(arr):
    answer = -1

if answer != -1:
    print(*( [arr[0]] + [1] * (N - len(arr)) + arr[1:]),end = "")
else:
    print(answer)
