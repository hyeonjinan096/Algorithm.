const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
//2.44
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let t = Number(input.shift());
let visited = [];
let values = [];
const bfs = (n) => {
  visited.push(n);
  q = [n];
  while (q.length) {
    cur = q.shift();
    if (values[cur] === n) {
      return true;
    }
    if (!visited.includes(values[cur])) {
      visited.push(cur);
      q.push(values[cur]);
    }
  }
  return false;
};

for (let i = 0; i < t; i++) {
  let n = Number(input.shift());
  values = input
    .shift()
    .split(" ")
    .map(e => Number(e));
  values.unshift(0);
  let cnt = 0;
  visited = [];
  for (let i = 1; i < values.length; i++) {
    if (!visited.includes(i)) {
      bfs(i, values) && cnt++;
    }
  }
  console.log(cnt);
}
