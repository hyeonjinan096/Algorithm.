const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
//12.31
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let [x, y] = input
  .shift()
  .split(" ")
  .map(e => Number(e));
let i = 0;

let values = [];
for (let i = 1; i < x + 1; i++) {
  values.push(i);
}

let s = 0; //0부터 시작
let answer = [];

for (let j = 0; j < x; j++) {
  let check = 0;
  let i = s - 1;
  while (1) {
    i++;
    let k = i % x;
    if (values[k] === 0) continue;
    check++;
    if (check === y) {
      values[k] = 0;
      answer.push(k + 1);
      s = k + 1;
      break;
    }
  }
}

console.log("<" + answer.join(", ") + ">");
