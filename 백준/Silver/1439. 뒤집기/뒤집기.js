const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
//6.53
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const values = input[0].split("").map(e => Number(e));

let flag = values[0];
let o = 0;
let z = 0;
flag === 0 ? z++ : o++;
for (let i = 0; i < values.length; i++) {
  if (values[i] !== flag) {
    flag === 0 ? o++ : z++;
    flag === 0 ? (flag = 1) : (flag = 0);
  }
}
console.log(Math.min(o, z));
