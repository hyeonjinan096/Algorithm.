const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const n = Number(input.shift());

let [cnt, sum, start, end] = [0, 0, 0, 0];

while (end <= n) {
  if (sum < n) {
    end++;
    sum += end;
  } else if (sum > n) {
    sum -= start;
    start++;
  } else {
    cnt++;
    end++;
    sum += end;
    sum -= start;
    start++;
  }
}

console.log(cnt);
