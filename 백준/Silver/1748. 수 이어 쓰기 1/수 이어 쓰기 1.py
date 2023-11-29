n = input()
l = len(n) - 1
result = 0

for i in range(l):
    result += 9 * (10**i) * (i+1)
result += ((int(n) - (10 ** l))+1) * (l+1)

print(result)