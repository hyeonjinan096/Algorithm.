const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")

let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let N = Number(input.shift());

let arr = Array.from(Array(N), () => 0);
arr[0] = Number(input.shift());

for (let i = 1; i < N; i++) {
  let c = Number(input.shift());
  arr[i] = c * arr[i - 1] < c ? c : c * arr[i - 1];
}

console.log(Math.max(...arr).toFixed(3));
