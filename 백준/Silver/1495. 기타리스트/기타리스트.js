const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, s, m] = input[0].split(" ").map(e => Number(e));
const v = input[1].split(" ").map(e => Number(e));

const list = Array.from(Array(n + 1), () => new Array(m + 1).fill(0));

list[0][s] = 1;

for (let i = 1; i < n + 1; i++) {
  //음악을 돌기
  for (let j = 0; j < m + 1; j++) {
    //볼륨 돌기
    if (list[i - 1][j + v[i - 1]] === 1) {
      list[i][j] = 1;
    } else if (list[i - 1][j - v[i - 1]] === 1) {
      list[i][j] = 1;
    }
  }
}

let answer = -1;
list[n].forEach((e, i) => {
  if (e) answer = i;
});

console.log(answer);

