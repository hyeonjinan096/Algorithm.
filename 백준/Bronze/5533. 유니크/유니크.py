n = int(input())
first = []
second = []
third = []
for i in range(n):
    a, b, c = map(int, input().split())
    first.append(a)
    second.append(b)
    third.append(c)
for j in range(n):
    score = 0
    if first.count(first[j]) == 1:
        score += first[j]
    if second.count(second[j]) == 1:
        score += second[j]
    if third.count(third[j]) == 1:
        score += third[j]
    print(score)