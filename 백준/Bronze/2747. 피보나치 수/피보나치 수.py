N = int(input())
fibonacci = [0,1]

for _ in range(2,N+1):
    fibonacci.append(fibonacci[_-2] + fibonacci[_-1])

print(fibonacci[N])