function solution(board, skill) {
    var answer = 0;
    let N = board.length
    let M = board[0].length
    let tmp_board = [...Array(N+1)].map(()=> Array(M+1).fill(0))
    
    for (let [type, x,y,x2,y2,d] of skill){
        if (type == 1) d = -d
        tmp_board[x][y] += d
        tmp_board[x2+1][y2+1] += d
        tmp_board[x][y2+1] += -d
        tmp_board[x2+1][y] += -d
    }
    
    for (let i = 0;i<N;i++){
        for (let j=1; j< M;j++){
            tmp_board[i][j]+=tmp_board[i][j-1]
        }
    }
    for (let i=1;i<N;i++){
        for (let j =0;j<M;j++){
            tmp_board[i][j]+=tmp_board[i-1][j]
        }
    }
    
    for (let i=0;i<N;i++){
        for (let j = 0;j<M;j++){
            if (tmp_board[i][j] + board[i][j] > 0) answer++
        }
    }

    return answer;
}

//누적합을 이용해서 푸는 문제 입니다. 
//누적합 적용 위치 
//(x,y) ~ (x2, y2) a
// x,y/x2+1,y2+1 = a
// x,y2+1/x2+1,y = -1

//for문 돌면서 왼쪽 ~ 오른쪽
//for문 돌면서 위 ~ 아래

//원본 + new
//양수 갯수 세기



//파괴되지 않은 거눌의 수 리턴
