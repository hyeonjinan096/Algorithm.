N, b = map(int, input().split())
if N <= 2**(b+1) - 1:
    result = 'yes'
else:
    result = 'no'
print(result)
