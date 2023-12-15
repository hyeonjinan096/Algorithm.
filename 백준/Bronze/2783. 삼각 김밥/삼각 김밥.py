X, Y = map(int, input().split())

value = X*1000 / Y
N = int(input())

for i in range(N) :
    A, B = map(int, input().split())
    value2 = A*1000 / B
    if value > value2 :
        value = value2

print(round(value, 2))