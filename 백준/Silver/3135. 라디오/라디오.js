const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [a, b] = input
  .shift()
  .split(" ")
  .map(e => Number(e));

const n = Number(input.shift());
const arr = input.map(e => Number(e));

let min = Math.abs(a - b);
let asnwer = min;
for (let i = 0; i < arr.length; i++) {
  let d = Math.abs(b - arr[i]);
  if (min > d) {
    min = d;
    asnwer = d + 1;
  }
}
console.log(asnwer);

//구현
//min갱신
