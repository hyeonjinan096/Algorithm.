def solution(board, skill):
    n,m, cnt = len(board), len(board[0]),0
    sumtable = [[0]*(m+1) for _ in range(n+1)]
    for t, x1,y1,x2,y2, d in skill:
        if t == 1:
            d = -d
        sumtable[x1][y1] +=d
        sumtable[x2+1][y2+1] +=d
        sumtable[x1][y2+1]-=d
        sumtable[x2+1][y1]-=d 
    for i in range(n+1): # 위에서 아래로
        for j in range(m):
            sumtable[i][j+1]+=sumtable[i][j]
    for j in range(m+1): #왼쪽에서 오른쪽
        for i in range(n):
            sumtable[i+1][j]+=sumtable[i][j]
    return sum([1 for i in range(n) for j in range(m) if board[i][j]+ sumtable[i][j]>0])