const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
//6.53
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const n = Number(input.shift());
let values = input[0].split(" ").map(e => Number(e));

let dp = Array.from(Array(n), () => 1);

for (let i = 0; i < values.length; i++) {
  for (let j = 0; j < i; j++) {
    if (values[j] < values[i]) dp[i] = Math.max(dp[i], dp[j] + 1);
  }
}

console.log(Math.max(...dp));
