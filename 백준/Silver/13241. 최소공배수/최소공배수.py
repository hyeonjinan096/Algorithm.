import sys

a, b = map(int, input().split())

def gcd(a, b):
    while b:
        M = b
        b = a % b
        a = M
    return a

print(a*b//gcd(a, b))