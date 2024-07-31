const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [S, K] = input[0].split(" ").map(e => Number(e));
let answer = 1;

const n = Math.floor(S / K);
let r = S % K;

for (let i = 1; i <= K; i++) {
  if (r != 0) {
    r--;
    answer *= n + 1;
  } else {
    answer *= n;
  }
}

console.log(answer);
