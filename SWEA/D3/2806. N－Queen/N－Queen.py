T = int(input())

def dfs(x):
    global answer,N
    if x == N:
        answer+=1
        return
    for y in range(N): #0행의 열을 돈다.
        if y not in visited[0] and (y-x) not in visited[1] and (y+x) not in visited[2]:
          visited[0].append(y)
          visited[1].append(y-x) #차
          visited[2].append(y+x) #합
          dfs(x+1)
          visited[0].pop()
          visited[1].pop()
          visited[2].pop()
        

for test_case in range(1, T + 1):
    N = int(input())
    visited = [[],[],[]] #열, 오른쪽 대각선, 왼쪽 대각선
    answer = 0
    dfs(0)

    print(f'#{test_case} {answer}')