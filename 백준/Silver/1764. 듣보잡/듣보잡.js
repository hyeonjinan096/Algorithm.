const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
//12.31
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
input.shift();
const set = new Set(input);
console.log(input.length - set.size);
const answer = [];
input.forEach(e => {
  if (set.has(e)) {
    set.delete(e);
  } else {
    answer.push(e);
  }
});
console.log(answer.sort().join("\n"));
