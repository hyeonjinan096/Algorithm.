const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
//12.17
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let t = Number(input.shift());

for (let i = 0; i < t; i++) {
  let [n, m] = input.shift().split(" ").map(Number);
  let lst = input.shift().split(" ").map(Number);
  let q = lst.map((e, i) => [e, i]);
  let priority = lst.sort((a, b) => b - a);

  let cnt = 1;
  while (q.length) {
    let [p, i] = q.shift();
    if (p < priority[0]) {
      q.push([p, i]);
    } else {
      if (i === m) {
        console.log(cnt);
        break;
      }
      priority.shift();
      cnt++;
    }
  }
}
