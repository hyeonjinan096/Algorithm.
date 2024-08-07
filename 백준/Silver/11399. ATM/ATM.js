const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
//6.53
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const n = Number(input.shift());
const values = input[0].split(" ").map(e => Number(e));

values.sort((a, b) => a - b);

let answer = values[0];

for (let i = 1; i < values.length; i++) {
  values[i] += values[i - 1];
  answer += values[i];
}

console.log(answer);
