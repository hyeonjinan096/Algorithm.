T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(map(int,list(input()))) for _ in range(N)]

    mid = N//2
    answer = sum(graph[mid])
    
    x = 0
    y = N-1

    for i in range(mid):
        answer +=sum(graph[x][mid-i:mid+i+1])
        answer +=sum(graph[y][mid-i:mid+i+1])
        x+=1
        y-=1

    print(f'#{test_case} {answer}')
    