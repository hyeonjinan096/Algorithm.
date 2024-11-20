const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

const N = Number(input.shift());
const values = [];
const values2 = [];

for (let i = 0; i < N; i++) {
  lst = input.shift().trim().split("");
  values.push([...lst]);
  values2.push([...lst]);
}

const dir = [
  [1, 0],
  [-1, 0],
  [0, 1],
  [0, -1],
];

bfs = (x, y, c, data) => {
  q = [[x, y]];
  data[x][y] = "v";
  while (q.length) {
    [cx, cy] = q.shift();
    for (let [dx, dy] of dir) {
      let nx = cx + dx;
      let ny = cy + dy;

      let isOk = false;
      if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
        continue;
      }

      if (data[nx][ny] === "v") {
        continue;
      }
      for (color of c) {
        if (data[nx][ny] === color) {
          isOk = true;
          break;
        }
      }
      if (isOk) {
        data[nx][ny] = "V";
        q.push([nx, ny]);
      }
    }
  }
};

//적록색약 아닌 사람 구역
let sum1 = 0;
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (values[i][j] !== "V") {
      bfs(i, j, [values[i][j]], values);
      sum1 += 1;
    }
  }
}

//적록색약 아닌 사람 구역
let sum2 = 0;
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (values2[i][j] != "V") {
      if (values2[i][j] == "R" || values2[i][j] == "G") {
        bfs(i, j, ["R", "G"], values2);
      } else {
        bfs(i, j, ["B"], values2);
      }

      sum2 += 1;
    }
  }
}

console.log(sum1, sum2);
