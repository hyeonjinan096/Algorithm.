T = 10

for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(input()) for _ in range(8)]
    answer = 0

    for i in range(8):
      for j in range(9-N):
        if graph[i][j:j+N] == graph[i][j:j+N][::-1]:
          answer+=1
        sub = []
        for k in range(j,j+N):
          sub.append(graph[k][i])
        if sub == sub[::-1]:
          answer+=1
    
    print(f'#{test_case} {answer}')
