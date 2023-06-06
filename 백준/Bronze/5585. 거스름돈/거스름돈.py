import sys

n = 1000-int(sys.stdin.readline())

moneys = [500, 100, 50, 10, 5, 1]
count = 0

for money in moneys:
    if n == 0:
        break
    
    count += n // money #금액이 큰 거스름돈 먼저 잔돈 개수 계산
    n %= money
    
print(count)