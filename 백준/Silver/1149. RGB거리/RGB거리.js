const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
//6.53
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const n = Number(input.shift());
const values = input.map(e => e.split(" ").map(e => Number(e)));

dp = Array.from(Array(n), () => new Array(3).fill(0));

for (let i = 0; i < n; i++) {
  if (i === 0) {
    dp[0][0] = values[0][0];
    dp[0][1] = values[0][1];
    dp[0][2] = values[0][2];
    continue;
  }
  dp[i][0] = Math.min(dp[i - 1][1] + values[i][0], dp[i - 1][2] + values[i][0]);
  dp[i][1] = Math.min(dp[i - 1][0] + values[i][1], dp[i - 1][2] + values[i][1]);
  dp[i][2] = Math.min(dp[i - 1][0] + values[i][2], dp[i - 1][1] + values[i][2]);
}

console.log(Math.min(...dp[n - 1]));
