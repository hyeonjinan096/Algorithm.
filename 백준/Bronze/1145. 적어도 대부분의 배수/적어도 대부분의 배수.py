import sys

N = list(map(int, sys.stdin.readline().split()))


num = 2
while(1):
    cnt = 0
    for i in N:
        if num % i == 0:
            cnt += 1

    if cnt >= 3:
        print(num)
        break
    num +=1