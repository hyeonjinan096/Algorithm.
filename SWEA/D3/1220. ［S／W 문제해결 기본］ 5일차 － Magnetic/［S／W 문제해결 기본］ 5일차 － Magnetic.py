
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(map(int,input().strip().split(' '))) for _ in range(N)]
    answer=0

    for i in range(N):
        flag = 0
        for j in range(N):
            if graph[j][i] == 1:
                flag = 1
            if flag == 1 and graph[j][i] == 2:
                answer+=1
                flag = 0
    
    print(f'#{test_case} {answer}')