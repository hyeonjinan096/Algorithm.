n = input()
c = 0

while len(n) >= 2:
    t = 0
    for digit in n:
        t += int(digit)
    n = str(t)
    c += 1

print(c)

if int(n) % 3 == 0:
    print("YES")
else:
    print('NO')
