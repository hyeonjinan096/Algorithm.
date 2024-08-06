const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
//6.53
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const n = Number(input.shift());
let values = input[0].split(" ").map(e => Number(e));
let max = Math.max(...values);

let dp = Array.from(Array(max + 1), () => 0);

for (let i of values) {
  for (let j = 0; j < i; j++) {
    if (dp[j] + 1 > dp[i]) dp[i] = dp[j] + 1;
  }
}


console.log(Math.max(...dp));
