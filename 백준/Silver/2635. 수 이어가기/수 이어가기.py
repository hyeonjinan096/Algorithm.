N = int(input())
result = []

for second in range(1, 30000 + 1):
    i = [N, second]
    first = N

    while True:
        third = first - second
        if third < 0:
            break
        i.append(third)
        first = second
        second = third

    if len(result) < len(i):
        result = []
        result += i

print(len(result))
print(*result)
