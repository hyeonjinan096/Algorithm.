function solution(n) {
    var answer = 0;

    function bfs(x, y) {
        const visited = Array.from(Array(n), () => new Array(n).fill(false));
        const dx = [2, 2, -1, -1, 1, 1, -2, -2];
        const dy = [-1, 1, 2, -2, -2, 2, -1, 1];
        let count = 1;

        visited[x][y] = true;
        let queue = [[x, y]];
        while (queue.length > 0) {
            let [cx, cy] = queue.shift();
            for (let i = 0; i < 8; i++) { // 나이트의 8가지 이동 방향
                let next_x = cx + dx[i];
                let next_y = cy + dy[i];
                if (next_x >= 0 && next_x < n && next_y >= 0 && next_y < n) {
                    if (!visited[next_x][next_y]) {
                        visited[next_x][next_y] = true;
                        count++;
                        queue.push([next_x, next_y]);
                    }
                }
            }
        }

        return count;
    }

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (bfs(i, j) === n * n) {
                answer++;
            }
        }
    }

    return answer;
}

// 예시로 N=8인 경우를 호출하여 테스트
const result = solution(8);
console.log(result); // 결과 출력