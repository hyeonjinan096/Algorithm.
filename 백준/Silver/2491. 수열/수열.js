const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
//5.37//5.53
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const n = Number(input.shift());
let lst = input[0].split(" ").map(e => Number(e));

let plus = 1;
let minus = 1;
let answer = 0;
for (let i = 1; i < lst.length; i++) {
  if (lst[i] >= lst[i - 1]) plus++;
  else if (plus > 0) {
    answer = Math.max(answer, plus);
    plus = 1;
  }
  if (lst[i] <= lst[i - 1]) minus++;
  else if (minus > 0) {
    answer = Math.max(answer, minus);
    minus = 1;
  }
}

answer = Math.max(answer, minus);
answer = Math.max(answer, plus);
console.log(answer);
