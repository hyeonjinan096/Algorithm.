const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
//12.17
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let n = Number(input.shift());
let Map = input.map(e => e.trim().split(""));

let answer = Array.from(Array(n), () => []);

let bfs = (x, y) => {
  dir = [
    [1, 1],
    [1, -1],
    [1, 0],
    [0, 1],
    [0, -1],
    [-1, 1],
    [-1, -1],
    [-1, 0],
  ];

  let sum = 0;

  for ([dx, dy] of dir) {
    nx = x + dx;
    ny = y + dy;
    if (0 <= nx && nx < n && 0 <= ny && ny < n) {
      if (Map[nx][ny] != ".") {
        sum += Number(Map[nx][ny]);
      }
    }
  }

  return sum;
};

for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (1 <= Number(Map[i][j]) && Number(Map[i][j]) <= 9) {
      answer[i].push("*");
    } else {
      let cnt = bfs(i, j);
      if (cnt >= 10) cnt = 'M';
      answer[i].push(cnt);
    }
  }
}


console.log(answer.map(e=>e.join('')).join('\n'));
