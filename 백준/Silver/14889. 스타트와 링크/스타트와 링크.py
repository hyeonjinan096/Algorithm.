import sys
N = int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [False for _ in range(N)]
result = float('inf')

def DFS(level, idx):
    global result
    if level == N/2:
        A = 0
        B = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += board[i][j]
                elif not visited[i] and not visited[j]:
                    B += board[i][j]
        result = min(result,abs(A-B))
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            DFS(level+1, i+1)
            visited[i] = False



DFS(0,0)
print(result)