const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
//6.53
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const t = Number(input.shift());

const func = (n, values) => {
  let max = values[n - 1];
  let sum = 0;
  for (let i = n - 2; i >= 0; i--) {
    if (max > values[i]) {
      sum += max - values[i];
    } else {
      max = values[i];
    }
  }
  return sum;
};

for (let i = 0; i < t; i++) {
  const n = Number(input.shift());
  const values = input
    .shift()
    .split(" ")
    .map(e => Number(e));
  console.log(func(n, values));
}
