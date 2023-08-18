import sys  

a, b = map(int, sys.stdin.readline().split())

def gcd(x,y):
    k = x % y
    while k >0:
        x = y
        y = k
        k = x % y
    return y    
    
c = a * b // gcd(a,b)
print(gcd(a, b))
print(c)