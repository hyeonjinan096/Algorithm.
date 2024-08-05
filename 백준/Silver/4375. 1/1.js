const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const nums = input.map(e => Number(e));

const answers = [];

for (let i = 0; i < nums.length; i++) {
  const cur = nums[i];
  let num = 1; // 이 변수에 이전에 구한 값이 담기게 되는 것
  let length = 1;

  while (1) {
    if (num % cur === 0) {
      answers.push(length);
      break;
    } else {
      num = (num * 10 + 1) % cur; // 점화식
      length += 1; // 1을 한자리 더 추가함
    }
  }
}

console.log(answers.join('\n'));