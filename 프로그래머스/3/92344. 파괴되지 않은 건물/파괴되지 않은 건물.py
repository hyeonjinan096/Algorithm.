def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    sum_board = [[0]*M for _ in range(N)]

    #누적합 문제 이다.
    for t, r1, c1, r2, c2, d in skill:
        if t == 1:
            d = -d
        sum_board[r1][c1] += d
        if c2+1<M:
            sum_board[r1][c2+1] += -d
        if r2+1<N:
            sum_board[r2+1][c1] += -d
        if c2+1<M and r2+1<N:
            sum_board[r2+1][c2+1] += d

    for i in range(1,N):
        for j in range(M):
            sum_board[i][j]+=sum_board[i-1][j]
    for i in range(1,M):
        for j in range(N):
            sum_board[j][i]+=sum_board[j][i-1]
        
    for i in range(N):
        for j in range(M):
            board[i][j] +=sum_board[i][j]
        
    for b in board:
        for i in b:
            if i >0:
                answer+=1
    return answer

