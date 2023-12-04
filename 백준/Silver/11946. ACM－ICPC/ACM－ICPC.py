n, m, q = map(int, input().split())

problems = {}
for i in range(1, n + 1):
    for j in range(1, m + 1):
        problems[(i, j)] = [0, -1]  

for _ in range(q):
    log = input().split()
    problem_key = (int(log[1]), int(log[2]))
    if log[3] != 'AC':
        problems[problem_key][0] += 1
    elif problems[problem_key][1] < 0:
        problems[problem_key][1] = problems[problem_key][0] * 20 + int(log[0])

results = [[i, 0, 0] for i in range(1, n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if problems[(i, j)][1] >= 0:
            results[i - 1][1] += 1
            results[i - 1][2] += problems[(i, j)][1]

results.sort(key=lambda x: (-x[1], x[2], x[0]))

for result in results:
    print(*result)
