function solution(n) {
    let answer = 0;

    // 체스판을 2차원 배열로 초기화
    const board = Array.from({ length: n }, () => Array(n).fill(0));

    // 해당 위치에 퀸을 놓을 수 있는지 확인하는 함수
    function isSafe(row, col) {
        // 같은 열을 확인
        for (let i = 0; i < row; i++) {
            if (board[i][col] === 1) {
                return false;
            }
        }

        // 왼쪽 위 대각선 확인
        for (let i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] === 1) {
                return false;
            }
        }

        // 오른쪽 위 대각선 확인
        for (let i = row, j = col; i >= 0 && j < n; i--, j++) {
            if (board[i][j] === 1) {
                return false;
            }
        }

        return true;
    }

    // 퀸을 배치하는 함수 (백트래킹)
    function placeQueens(row) {
        if (row === n) {
            // 모든 퀸을 성공적으로 배치한 경우
            answer++;
            return;
        }

        for (let col = 0; col < n; col++) {
            if (isSafe(row, col)) {
                // 현재 위치에 퀸을 놓을 수 있다면
                board[row][col] = 1; // 퀸을 놓고
                placeQueens(row + 1); // 다음 행으로 이동
                board[row][col] = 0; // 백트래킹: 다른 경우를 위해 퀸을 제거
            }
        }
    }

    // 첫 번째 행부터 시작
    placeQueens(0);

    return answer;
}

// 예시로 N=8인 경우를 호출하여 테스트
const result = solution(8);
console.log(result); // N-Queens 문제의 해답 수 출력
