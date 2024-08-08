const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")

let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [x, y] = input[0].split(" ");

if (x.length !== y.length) {
  console.log(0);
} else {
  let answer = 0;
  for (let i = 0; i < x.length; i++) {
    if (  x[i] == y[i]) {
      if("8" == x[i]) answer++;
    }
    else {
      break;
    }
  }

  console.log(answer);
}
