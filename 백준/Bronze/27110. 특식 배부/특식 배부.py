N = int(input())
k = list(map(int, input().split()))
result = 0

for i in range(3) :
    if k[i] <= N :
        result += k[i]
    else :
        result += N

print(result)