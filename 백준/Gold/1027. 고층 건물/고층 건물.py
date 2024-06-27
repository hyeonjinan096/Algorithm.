N = int(input())

building = list(map(int, input().split()))
answer = 0

for i in range(N):
    temp = N - 1
    for j in range(i + 1, N):
        for k in range(i + 1, j):
            if building[k] - building[i] >= (((building[j] - building[i]) / (j - i)) * (k - i)):
                temp -= 1
                break
    for j in range(0, i):
        for k in range(j + 1, i):
            if building[k] - building[j] >= (((building[i] - building[j]) / (i - j)) * (k - j)):
                temp -= 1
                break
    answer = max(temp, answer)
print(answer)