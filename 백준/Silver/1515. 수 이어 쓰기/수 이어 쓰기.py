numbers = input()
i = 0
while True:
    i += 1
    n = str(i)
    while len(n) > 0 and len(numbers) > 0:
        if n[0] == numbers[0]:
            numbers = numbers[1:]
        n = n[1:]
    if numbers == '':
        print(i)
        break