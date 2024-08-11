const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
//12.31
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let [n, m] = input
  .shift()
  .split(" ")
  .map(e => Number(e));

let space = input.map(e =>
  e.split(" ").map(v => (v[0] === "1" ? -1 : Number(v)))
);
//모든 곳 순회
//각 노드마다 8방향으로 퍼짐 만나면 즉시 값 반환
//각 노드 visited에 값 저장
//visited된 노드 방문 시 거리 합치고 즉시 값 반환
//각 노드에 값 중 가장 최댓값 매 번 max에 저장해도 좋을 듯

dr = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
  [1, 1],
  [-1, 1],
  [1, -1],
  [-1, -1],
];
const bfs = (x, y) => {
  let q = [[x, y, 0]];
  let visited = Array.from(Array(n), () => new Array(m).fill(0));
  while (q.length) {
    [c_x, c_y, d] = q.shift();
    visited[c_x][c_y] = 1;
    for (let i = 0; i < 8; i++) {
      n_x = c_x + dr[i][0];
      n_y = c_y + dr[i][1];

      if (n_x < 0 || n_x > n - 1 || n_y < 0 || n_y > m - 1) continue;
      if (visited[n_x][n_y]) continue;

      visited[n_x][n_y] = 1;
      if (space[n_x][n_y] === -1) {
        return d + 1;
      } else {
        q.push([n_x, n_y, d + 1]);
      }
    }
  }
};

//visited따로 안만들고 저장

let max = 0;
for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (space[i][j] === 0) {
      space[i][j] = bfs(i, j);
      if (max < space[i][j]) max = space[i][j];
    };
  }
}

console.log(max);
