def solution(board, skill):
    answer = 0
    m = len(board)
    n = len(board[0])
    sum_board = [[0]*n for i in range(m)]
    
    for t, x, y, a, b, d in skill:
        if t == 1: d = -d
        if 0<=x<m and 0<=y<n:
            sum_board[x][y] += d
        if 0<=a+1<m and 0<=b+1<n:
            sum_board[a+1][b+1] += d
        if 0<=a+1<m and 0<=y<n:
            sum_board[a+1][y] += -d
        if 0<=x<m and 0<=b+1<n:
            sum_board[x][b+1] += -d
            
    for i in range(m):
        for j in range(0,n-1):
            sum_board[i][j+1] +=sum_board[i][j]
    for i in range(n):
        for j in range(0,m-1):
            sum_board[j+1][i] += sum_board[j][i]
    
    for i in range(m):
        for j in range(n):
            board[i][j]+=sum_board[i][j]
            if board[i][j] > 0:
                answer+=1
    
    
    
    
    return answer