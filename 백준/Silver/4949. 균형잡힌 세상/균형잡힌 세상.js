const fs = require("fs");
// TODO: 제출 시 경로 변환 필수
//12.31
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const check = str => {
  let stack = [];
  for (let i of str) {
    if (i === "(" || i === "[") {
      stack.push(i);
    } else if (i === ")" && stack.pop() !== "(") {
      return "no";
    } else if (i === "]" && stack.pop() !== "[") {
      return "no";
    }
  }
  return stack.length === 0 ? "yes" : "no";
};

for (let i = 0; i < input.length - 1; i++) {
  let str = input[i];
  console.log(check(str));
}
