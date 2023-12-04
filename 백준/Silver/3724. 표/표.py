for _ in range(int(input())):
    m, n = map(int, input().split())
    list = []
    for i in range(n):
        list.append([*map(int, input().split())])
    result = {}
    for i in range(m):
        y = 1
        for j in range(n):
            y *= list[j][i]
        result[y] = i+1
    print(result[max(result)])