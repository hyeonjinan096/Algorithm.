import math
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    data = list(input().split(' '))

    dx = 0
    dy = math.ceil(n/2)
    answer = []
    for i in range(n):
        if(i%2 == 0):
            answer.append(data[dx])
            dx+=1
        else:
            answer.append(data[dy])
            dy+=1
    print(f'#{test_case} ',end='')
    print(*answer)
        