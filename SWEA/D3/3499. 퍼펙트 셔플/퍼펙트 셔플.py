import math
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    cards = list(input().split())
    mid = math.ceil(N/2)
    answer = []

    for i in range(mid):
        answer.append(cards[i])
        if mid+i < N:
            answer.append(cards[mid+i])

    print(f'#{test_case} ',end ='')
    print(*answer)