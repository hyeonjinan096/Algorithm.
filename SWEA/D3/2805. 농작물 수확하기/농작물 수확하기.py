T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(map(int,list(input()))) for _ in range(N)]

    answer = 0
    start = N//2
    end = N//2+1 
    for i in range(N//2):
      answer += sum(graph[i][start:end])
      start-=1
      end+=1
    start = N//2
    end = N//2+1
    for i in range(N-1,N//2,-1):
      answer += sum(graph[i][start:end])
      start-=1
      end+=1
    
    answer += sum(graph[N//2])
    print(f'#{test_case} {answer}')


