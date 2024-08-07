const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
//6.53
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const values = input[0].split("").map(e => Number(e));

let cnt = 0;

for (let i = 0; i < values.length - 1; i++) {
  if (values[i] !== values[i + 1]) {
    cnt++;
  }
}
console.log(Math.floor((cnt + 1) / 2));
