import sys

while (1):
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    answer = 0
    carry = 0

    while (n > 0 or m > 0):
        a = n % 10
        b = m % 10
        if a + b + carry >= 10:
            carry = 1
            answer += 1
        else:
            carry = 0
        n = n // 10
        m = m // 10

    print(answer)





