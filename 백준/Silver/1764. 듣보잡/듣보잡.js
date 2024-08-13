const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
//12.31
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let [n, m] = input.shift().split(" ").map(Number);

let a = new Set(input.slice(0, n));
let b = input.slice(n);

let answer = [];

for (let i = 0; i < m; i++) {
  if (a.has(b[i])) {
    answer.push(b[i]);
  }
}

answer.sort();
console.log(answer.length);
console.log(answer.join("\n"));
